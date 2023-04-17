# Here we have used out tracking code as a module to show how we can use it on different aspects 

import cv2
import mediapipe as mp
import time
import handTrackingModule as htm

pTime =0
cTime =0
cap =cv2.VideoCapture(0)
detector=htm.handDetector()


while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img)
    if len(lmList) !=0:
        print(lmList[4])


    cTime = time.time()  # it gives the current time


    fps = 1/(cTime-pTime)# for megapixels it is created to calculate
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)



    cv2.imshow("Image",img)
    cv2.waitKey(1)



