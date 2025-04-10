from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
import os
import torch
import torchvision.transforms as T
import numpy as np
import nibabel as nib
import segmentation_models_pytorch as smp
import tempfile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = torch.load('C:/Users/Amir/Desktop/IPRIA-hackathon-AmirHossein-Mahjoub-Khorasani/unet.pt', 
                   map_location=device, 
                   weights_only=False)
model.eval()

transform = T.Compose([
    T.ToPILImage(),
    T.Resize((224, 224)),
    T.ToTensor(),
])

def calculate_EF(ed_vol_2CH, es_vol_2CH, ed_vol_4CH, es_vol_4CH):
    
    EDV = (ed_vol_2CH + ed_vol_4CH) / 2
    ESV = (es_vol_2CH + es_vol_4CH) / 2

    EF = ((EDV - ESV) / EDV) * 100
    return EF

def calculate_volume(img_path):
    data = nib.load(img_path).get_fdata()
    data_t = transform(data)
    data_t = data_t.unsqueeze(0)

    with torch.no_grad():
        mask = model(data_t)
        
    mask = torch.nn.functional.interpolate(mask, 
                                           size=(data.shape[0], data.shape[1]), 
                                           mode='bilinear', 
                                           align_corners=False)
    mask = np.array(mask)
    mask = (mask[0, 1, :, :] > 0).astype(np.uint8)  
    pixel_to_mm = 0.308
    x_coords, y_coords = np.where(mask == 1)
    x_min, y_min = np.min(x_coords), y_coords[np.argmin(x_coords)]
    x_max, y_max = np.max(x_coords), y_coords[np.argmax(x_coords)]
    L = np.sqrt((x_max - x_min) ** 2 + (y_max - y_min) ** 2) * pixel_to_mm
    A_l = np.sum(mask) * (pixel_to_mm ** 2) 
    V = (8 * (A_l ** 2)) / (3 * np.pi * L)

    return V

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/")
async def upload_file(files: List[UploadFile] = File(...)):
    volumes = []
    for file in files:
        if not file.filename.endswith('.nii.gz'):
            raise HTTPException(status_code=400, detail='only ".nii.gz" files are allowed')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".nii.gz") as temp_file:
            temp_path = temp_file.name
            print(temp_path)
            shutil.copyfileobj(file.file, temp_file)
        try:
            volume = calculate_volume(temp_path)
            volumes.append(volume)
        finally:
            os.unlink(temp_path) 
    if len(volumes) != 4:
        raise HTTPException(status_code=400, detail="Please upload just 4 files: (ED 2CH, ES 2CH, ED 4CH, ES 4CH)")
        
    ef = calculate_EF(volumes[0], volumes[1], volumes[2], volumes[3])
    return {'message': f'ef = {ef:.2f}%'}