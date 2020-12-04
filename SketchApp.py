import cv2
import numpy as np
def getmysketch(image):
  # convert the captured image into gray scale image 
  grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  
  # blurring the image
  blurimg=cv2.GaussianBlur(grayimg,(3,3),0)
  
  # extracting edges
  edges=cv2.Canny(blurimg,10,80)
  
  # Capturing video from webcam
  ret,mimg=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
  return mimg

# It performs the function to open the webcam and to capture the video.
vid_capt=cv2.VideoCapture(0)

while True:
   #It captures the video frame by frame
   ret,pic_capt=vid_capt.read()
  
   #To display the sketch it calls the function as shown 'getmysketch(frame)' 
   cv2.imshow('Your Sketch',getmysketch(pic_capt))
  
   #It breaks the ongoing activity and closes the dialog box after pressing the enter button.
   if cv2.waitKey(1)==13:
      break
     
   
   
  
