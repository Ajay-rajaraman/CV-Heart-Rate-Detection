import cv2
import face_recognition
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from vidstab import VidStab
from scipy.signal import find_peaks




def face_extraction(frame):
    faces=face_cascade.detectMultiScale(frame,1.1,4)
    
    for (x,y,h,w) in faces:
        cv2.rectangle(frame,(x, y),(x+w,y+h),(255,0,0),4)
    return frame

def DetectionAndExtraction_of_ROI(frame):
    face_locations = face_recognition.face_locations(frame)
    face_landmarks_list = face_recognition.face_landmarks(frame)
    for face_location in face_locations:
        top,right,bottom,left =face_location
        bottom=34
        k = face_landmarks_list[0]['right_eyebrow']
        bottom= face_landmarks_list[0]['right_eyebrow'][0][1]
        for k1 in k :
            if(bottom>k1[1]):
                bottom=k1[1]
        k = face_landmarks_list[0]['left_eyebrow']
        lbottom= face_landmarks_list[0]['left_eyebrow'][0][1]
        for k1 in k : 
            if(lbottom>k1[1]):
                lbottom=k1[1]
        bottom=min(bottom,lbottom)
        a,b=(left+40,top)
        c,d=(right-40,bottom)
        cv2.rectangle(frame,(a,b),(c,d),(255,255,0),4)
        
        im=Image.fromarray(f)
    try:
        ROI = im.crop((a,b,c,d))
        ROI_array=np.array(ROI)
        ROI_array[:,:,0]=0
        ROI_array[:,:,2]=0
        x,y=ROI_array[:,:,1].shape
        mean_green=(sum(sum(ROI_array[:,:,1]))/(x*y))
        green_array.append(mean_green)
    except:
        try:
            green_array.append(green_array[count-1])
        except:
            green_array.append(0)
    
        return frame,green_array
    
def signal_processing(green_array):
    freq=count
    freq_division=fps/freq
    f=np.arange(0,fps,freq_division)
    signal=[]
    averageOfMean=sum(green_array)/len(green_array)
    for i in green_array:
        signal.append(i-averageOfMean) 
        
    fftsignal=fft(signal)
    
    highpass=0.66
    lowpass=4
    LowElementReject=round(highpass/freq_division)
    HighElementReject=round(lowpass/freq_division)
    fftsignal[1:LowElementReject]=0
    fftsignal[HighElementReject:freq]=0
    signal_filtered=ifft(fftsignal)
    peaks, _ = find_peaks(signal_filtered, height=0.1)
    time=count/fps
    BPM =len(peaks)*(60)/time
    peaks.sort()
    hrv=[]
    for i in range(len(peaks)+1):
        try:
            hrv_value=peaks[i+1]-peaks[i]
            hrv_in_sec=hrv_value/fps
            hrv.append(hrv_in_sec)
        except:
            break
    print("Heart rate:",round(BPM))
    print(hrv)
    plt.plot(signal_filtered)
    
    
    return hrv,BPM
        
    
    
    
# Initialization of variables
cap = cv2.VideoCapture("../InputVideos/ajay.mp4")
fps=cap.get(cv2.CAP_PROP_FPS)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count=0  
green_array=[] 
stabilizer = VidStab() 

if cap.isOpened() == False:
    print('error')
   
# Getting each frame of the video
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        
        frame=cv2.resize(frame,(600,400))
        
        frame = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        face_extraction(frame)
        
        f=frame.copy()
        
        count=count+1
        
        frame = stabilizer.stabilize_frame(input_frame=frame, border_size=20)
        
        DetectionAndExtraction_of_ROI(frame)
        
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            
            break
        
    else:
        
        break
    
cap.release()

cv2.destroyAllWindows()

signal_processing(green_array)


        
        
        
        
        
