# Calculating-Cardiac-Ejection-Fraction-Using-Echocardiography-Image-Segmentation
This project utilizes a U-Net model for heart image segmentation, enabling the calculation of heart volume necessary for ejection fraction (EF) estimation. The volume is computed using Simpson’s single plane formula, providing a robust approach for cardiac analysis.

## Idea description
In recent years, significant advancements have occurred in the fields of image processing and deep learning, particularly impacting medicine and disease diagnosis. One of the most important and challenging issues in medical imaging is the segmentation of the heart in images. This process refers to the identification and separation of different regions of the heart in medical images, especially in echocardiographic images. Accurate segmentation of the heart can help physicians better understand cardiac function and provide more precise diagnoses.

In this context, the calculation of Ejection Fraction (EF) emerges as a key metric in assessing heart performance. EF is the percentage of blood in the left ventricle that is pumped out with each heartbeat and serves as a vital marker for diagnosing heart failure and other cardiac disorders. Therefore, accuracy in cardiac image segmentation not only enhances diagnostic quality but also aids physicians in clinical and therapeutic decision-making.

Among the tools used for this purpose, Convolutional Neural Networks (CNNs), particularly advanced architectures like U-Net, have been recognized as effective in segmenting medical images. U-Net, due to its specific structure, which includes encoder-decoder layers, is capable of accurately extracting various features from images while preserving spatial information. These characteristics make U-Net particularly suitable for segmenting images with small dimensions and complex details, such as cardiac images.

After segmenting the inner region of the left ventricle using the U-Net network, the volume needs to be calculated. The volume of the left ventricle is computed using the Simpson’s single plane method, which is a technique for calculating the volume of the left ventricle from images, and ultimately EF is calculated for each patient.

The dataset used in this challenge is the Multi-Acquisitions Cardiac Ultrasound Segmentation (CAMUS) dataset, collected from the University Hospital of Etienne St in France. The images were collected from 500 patients in both 2D, two-chamber, and four-chamber views, and manual segmentation has been performed for each of these images.

The segmented regions in the ventricle are divided into the following areas:

- 1) Left ventricular outer wall (myocardium)
- 2) Inner region of the ventricle (endocardium)
- 3) Left atrium (atrium left)

## Description of the model used
Using U-Net for heart image segmentation allows us to accurately identify different regions of the heart, thereby facilitating precise EF calculation. The structure of the U-Net network is divided into three parts:

- 1) Encoder: The first part of U-Net, responsible for extracting features from the input image. This section typically includes convolutional layers and pooling layers that reduce the dimensions of the image and extract high-level features.

- 2) Decoder: The second part of U-Net, responsible for reconstructing the segmented image. This section generally includes upsampling layers and convolutional layers that return the dimensions of the image to its original state.

- 3) Skip Connections: One of the key features of U-Net is the use of direct connections between the encoder and decoder layers. This helps preserve local information and details during the reconstruction process.

In the encoder part of this model, the 1b-EfficientNet network is used, which is a neural network model designed for optimizing accuracy and efficiency. This model is particularly applicable in image recognition and classification tasks and is used here as a feature extractor.

Features of EfficientNet include its scalability and high efficiency. For example, EfficientNet uses a scalable approach to increase the dimensions of the network instead of merely increasing the number of layers. This means increasing depth, width, and image resolution simultaneously. Additionally, pre-trained weights from ImageNet are used for this EfficientNet network. The pre-trained weights refer to weights trained on the ImageNet dataset. Using these pre-trained weights allows new models to benefit from learned features in large datasets. This is especially useful when there is less data available. Furthermore, models that start from pre-trained weights usually achieve higher accuracy faster and reduce the need for training from scratch.

To calculate EF and solve this problem, we need to segment the inner region of the ventricle (endocardium) to estimate the volume output from the heart. However, after evaluations, it was decided to segment all four regions (including a background region).

In this implementation, the U-Net network is used, and for training the model, two-chamber and four-chamber images of each patient’s heart during two time points (End Diastole - ED and End Systole - ES) are utilized, allowing the model to segment these images at the two primary times for EF calculation.

The metric and loss function used for training the model is Dice. Dice is a similarity measurement metric used to assess the overlap between two sets. This metric is very popular in image segmentation, especially in medical imaging where high accuracy is required.

The optimization algorithm used to solve this problem is the Adam optimizer. The Adam optimizer generally operates faster than other optimization algorithms and performs well in large and complex problems, as well as in situations where gradients are unstable.

To calculate EF, the two-chamber and four-chamber heart images must first be provided to the model at both ED and ES times, producing the segmented images. Then, the number of pixels in the left ventricle’s inner region is calculated at ED and ES times, and according to Simpson’s single plane method, the volume of the inner region of the ventricle is computed, leading to the calculation of the patient’s EF.

## API and Web Interface
To facilitate the use of this model, a simple RESTful API has been developed using FastAPI. This API allows users to upload echocardiographic images and receive segmentation results along with EF calculation. It serves as a lightweight and accessible way to interact with the model without needing deep technical knowledge.

Additionally, a basic web interface is provided using HTML, CSS, and JavaScript, enabling users to interact with the system visually and upload images directly through their browser. This front-end is designed to be user-friendly and helps demonstrate the practical application of the model in a real-world setting.

## Thank You for Exploring This Project!
I appreciate your interest in my project on heart image segmentation and ejection fraction measurement.

If you have any questions, suggestions, or feedback, please feel free to reach out. Together, we can contribute to the advancement of medical imaging and make a difference in the field of cardiology.

Let’s innovate for a healthier tomorrow!

Happy Coding! ❤️
