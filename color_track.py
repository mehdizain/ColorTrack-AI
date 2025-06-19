import os 
import cv2
import numpy as np
from PIL import Image
vid=cv2.VideoCapture(0)

while True:
    ret,frame=vid.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_limit=np.array([100,150,50])
    upper_limit=np.array([130,255,255])
    
    mask=cv2.inRange(hsv,lower_limit,upper_limit)

    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt)>1000:
            x1,y1,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,255,0),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()