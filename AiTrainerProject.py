import cv2
import numpy as np
import time
import PoseEstimationModule as pm


cap= cv2.VideoCapture(r"D:\PYTHON\projects\Personal Ai Trainer\videos\manLifting.mp4")
# img=detector.findPose(img,draw=True)
detector = pm.poseDetector()
count = 0
dir =0

while True:
    success, img = cap.read()
    #img = cv2.resize(img,(720,1280))
    #img = cv2.imread(r"D:\PYTHON\projects\Personal Ai Trainer\videos\pexels-tima-miroshnichenko-5327469.jpg")
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    #print(lmList)
    if len(lmList)!=0:
        #right arm
        detector.findAngle(img,12,14,16)
        # #left arm
        # detector.findAngle(img,11,13,15)
        angle=detector.findAngle(img,12,14,16)
        per =np.interp(angle,(55,165),(100,0))
        bar = np.interp(angle,(55,165),(100,650))
        #print(angle,per)

        #check for dumble curls
        color = (255,0,255)

        if per ==100:
            color=(0,255,0)
            if dir ==0:
                count+=0.5
                dir=1
        if per ==0:
            color=(255,0,255)
        
            if dir==1:
                count+=0.5
                dir=0
        print(count)

        #cv2.circle(img,(200,450),70,(0,255,0),cv2.FILLED)
        
        cv2.rectangle(img,(1100,100),(1175,650),color,3)
        cv2.rectangle(img,(1100,int(bar)),(1175,650),color,cv2.FILLED)
        cv2.putText(img,f'{int(per)} %',(1100,75),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0),4)
        
        #Draw curl count
        cv2.rectangle(img,(0,450),(250,720),(0,255,0),cv2.FILLED)
        cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
        
    #img=cv2.resize(img,(720,500))

    cv2.imshow("Image",img)
    cv2.waitKey(1)
