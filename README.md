# Calculating-Cardiac-Ejection-Fraction-Using-Echocardiography-Image-Segmentation
This project utilizes a U-Net model for heart image segmentation, enabling the calculation of heart volume necessary for ejection fraction (EF) estimation. The volume is computed using Simpson’s single plane formula, providing a robust approach for cardiac analysis.

## Idea description
In recent years, significant advancements have occurred in the fields of image processing and deep learning, particularly impacting medicine and disease diagnosis. One of the most important and challenging issues in medical imaging is the segmentation of the heart in images. This process refers to the identification and separation of different regions of the heart in medical images, especially in echocardiographic images. Accurate segmentation of the heart can help physicians better understand cardiac function and provide more precise diagnoses.

In this context, the calculation of Ejection Fraction (EF) emerges as a key metric in assessing heart performance. EF is the percentage of blood in the left ventricle that is pumped out with each heartbeat and serves as a vital marker for diagnosing heart failure and other cardiac disorders. Therefore, accuracy in cardiac image segmentation not only enhances diagnostic quality but also aids physicians in clinical and therapeutic decision-making.

Among the tools used for this purpose, Convolutional Neural Networks (CNNs), particularly advanced architectures like U-Net, have been recognized as effective in segmenting medical images. U-Net, due to its specific structure, which includes encoder-decoder layers, is capable of accurately extracting various features from images while preserving spatial information. These characteristics make U-Net particularly suitable for segmenting images with small dimensions and complex details, such as cardiac images.

After segmenting the inner region of the left ventricle using the U-Net network, the volume needs to be calculated. The volume of the left ventricle is computed using the Simpson’s single plane method, which is a technique for calculating the volume of the left ventricle from images, and ultimately EF is calculated for each patient.

The dataset used in this challenge is the Multi-Acquisitions Cardiac Ultrasound Segmentation (CAMUS) dataset, collected from the University Hospital of Etienne St in France. The images were collected from 500 patients in both 2D, two-chamber, and four-chamber views, and manual segmentation has been performed for each of these images.

The segmented regions in the ventricle are divided into the following areas:

Left ventricular outer wall (myocardium)
Inner region of the ventricle (endocardium)
Left atrium (atrium left)
