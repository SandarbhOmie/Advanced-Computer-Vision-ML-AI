import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False,maxHands=2,modelComplexity=1,detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.modelComplex=modelComplexity
        self.detectionCon=detectionCon
        self.trackCon =trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplex,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgRGB =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
    
        # for multiple hands
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) # its is used to show the lines b/w the hand images.
        return img
    
    def findPosition(self,img,handNo=0,draw=True):
        
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h,w,c=img.shape # this wll give us width and height
                cx,cy = int(lm.x*w),int(lm.y*h) # this is the position of centre
                #print(id,cx,cy) # the id nuber will help indexing he landmarks
                lmList.append([id,cx,cy])

                if draw:# is means no. of point in the image tracking points (Red points) 
                    cv2.circle(img ,(cx,cy),10,(255,0,0),cv2.FILLED) # img is for image ,(cx,cy) is for the centre point of the image,(255,0,255) for color pink of circle, .FIllED is for filling the color to the circle
        
        return lmList

               
def main():
    pTime =0
    cTime =0
    cap =cv2.VideoCapture(0)
    detector=handDetector()


    while True:
        success,img=cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        if len(lmList) !=0:

            print(lmList[4])


        cTime = time.time()  # it gives the current time


        fps = 1/(cTime-pTime)# for megapixels it is created to calculate
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)



        cv2.imshow("Image",img)
        cv2.waitKey(1)




if __name__=="__main__":
    main()