import cv2
import numpy as np
import time
def draw_circle(event,x,y,flags,param):
    global pt1,clicked
    if event==cv2.EVENT_LBUTTONDOWN:
        if clicked==True:
            pt1=(0,0)
            clicked=False
        if clicked==False:
            pt1=(x,y)
            clicked=True
    
pt1=(0,0)
clicked=False

#CONNECTING FUNCITON
cap=cv2.VideoCapture('C:\\Users\\prati\\Downloads\\20-Seconds Animation.mp4')

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_circle)
if cap.isOpened()==False:
    print('ERROR OCCURED')

else:

    while cap.isOpened():
        ret,frame=cap.read()
        time.sleep(1/20)

        
        if clicked==True:
            cv2.circle(frame,pt1,50,color=(255,0,0),thickness=5)
        cv2.imshow('Test',frame)
        if cv2.waitKey(1)==ord('q'):
            break

        
cap.release()
cv2.destroyAllWindows()








