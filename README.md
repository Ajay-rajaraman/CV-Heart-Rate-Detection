# CV-Heart-Rate-Detection
Heart Rate Detection from Video Frames

## Overview
A person’s heart rate can be indicative of their health, fitness, activity level, stress, and much more. Cardiac pulse is typically measured in clinical settings using an electrocardiogram (ECG), which requires patients to wear chest straps with adhesive gel patches that can be abrasive and become uncomfortable for the user. Heart rate may also be monitored using pulse oximetry sensors that may be worn on the fingertip or earlobe. These sensors are not convenient for long-term wear and the pressure can become uncomfortable over time. So for this, we are using a non-contact means of measuring heart rate that could be beneficial for sensitive populations and can calculate pulse using a simple webcam or phone camera that could also be useful in telemedicine.


## How it works:
This application uses OpenCV to find the location of the user's face, then isolate the forehead region. Data is collected from this location over time to estimate the user's heart rate. This is done by measuring average optical intensity in the forehead location, in the subimage's green channel alone (a better color mixing ratio may exist, but the blue channel tends to be very noisy). Physiological data can be estimated this way thanks to the optical absorption characteristics of (oxy-) haemoglobin.With good lighting and minimal noise due to motion, a stable heartbeat should be isolated in about 15 seconds.



## Video link(2nd video under different light condition)

[Video link](https://photos.app.goo.gl/XB62J21rb6fjkNRg9)



