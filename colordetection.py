import cv2
from utils import get_limits
from PIL import Image

yellow=[0,255,255]
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()

    hsvimg=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lowerlimit,upperlimit=get_limits(color=yellow)
    mask=cv2.inRange(hsvimg,lowerlimit,upperlimit)
    mask_=Image.fromarray(mask)

    bbox=mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        img= cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),5)
    
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()