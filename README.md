# CV-Heart-Rate-Detection
Heart Rate Detection from Video Frames

## Overview
A person’s heart rate can be indicative of their health, fitness, activity level, stress, and much more. Cardiac pulse is typically measured in clinical settings using an electrocardiogram (ECG), which requires patients to wear chest straps with adhesive gel patches that can be abrasive and become uncomfortable for the user. Heart rate may also be monitored using pulse oximetry sensors that may be worn on the fingertip or earlobe. These sensors are not convenient for long-term wear and the pressure can become uncomfortable over time. So for this, we are using a non-contact means of measuring heart rate that could be beneficial for sensitive populations and can calculate pulse using a simple webcam or phone camera that could also be useful in telemedicine.


## How it works:
This application uses OpenCV to find the location of the user's face, then isolate the forehead region. Data is collected from this location over time to estimate the user's heart rate. This is done by measuring average optical intensity in the forehead location, in the subimage's green channel alone (a better color mixing ratio may exist, but the blue channel tends to be very noisy). Physiological data can be estimated this way thanks to the optical absorption characteristics of (oxy-) haemoglobin.With good lighting and minimal noise due to motion, a stable heartbeat should be isolated in about 15 seconds.

### Face detection 

![image](https://user-images.githubusercontent.com/66733698/116918022-05951080-ac6d-11eb-910c-94172019314f.png)

### ROI detection 

![image](https://user-images.githubusercontent.com/66733698/116918124-23fb0c00-ac6d-11eb-801c-3187741a32b0.png)


## Results

### fft(fourier transform)
![fft](https://user-images.githubusercontent.com/66733698/116918481-953abf00-ac6d-11eb-8e4d-a17f66719cc3.png)

###  bandpass_for_fft
![bandpass_for_fft](https://user-images.githubusercontent.com/66733698/116918751-ecd92a80-ac6d-11eb-8d9f-89bad38ce0f0.png)

### ifft(Inverse fourier transform)

![ifft](https://user-images.githubusercontent.com/66733698/116918833-09756280-ac6e-11eb-8a27-e4e79bb0979d.png)


## Video link
2nd video under different light condition:
[Video link](https://photos.app.goo.gl/XB62J21rb6fjkNRg9)


## Walkthrough Video link  
[video link](https://drive.google.com/file/d/1IaO12FuTq8LXjnS4QPOLCLarRw5Ha34k/view?usp=sharing)


