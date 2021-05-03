# CV-Heart-Rate-Detection
Heart Rate Detection from Video Frames

## Overview



## How it works:
This application uses OpenCV to find the location of the user's face, then isolate the forehead region. Data is collected from this location over time to estimate the user's heart rate. This is done by measuring average optical intensity in the forehead location, in the subimage's green channel alone (a better color mixing ratio may exist, but the blue channel tends to be very noisy). Physiological data can be estimated this way thanks to the optical absorption characteristics of (oxy-) haemoglobin.With good lighting and minimal noise due to motion, a stable heartbeat should be isolated in about 15 seconds.


## Requirements:
1)Python 
2)Opencv
3)Numpy, Scipy

## Video link

[Video link](https://photos.app.goo.gl/XB62J21rb6fjkNRg9)
