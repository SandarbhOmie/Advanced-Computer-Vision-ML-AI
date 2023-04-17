import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False,maxHands=2,detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon =trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgRGB =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
    
        # for multiple hands
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) # its is used to show the lines b/w the hand images.
        return img
                #     # here lm ois called as landmakr which is considered here just a reference point of the tracing sings
                #    for id, lm in enumerate(handLms.landmark):
                #        # print(id,lm)
                #         h,w,c=img.shape # this wll give us width and height
                #         cx,cy = int(lm.x*w),int(lm.y*h) # this is the position of centre
                #         print(id,cx,cy) # the id nuber will help indexing he landmarks
                #         #if id ==0: # is means no. of point in the image tracking points (Red points) 
                #         cv2.circle(img ,(cx,cy),15,(250,0,250),cv2.FILLED) # img is for image ,(cx,cy) is for the centre point of the image,(255,0,255) for color pink of circle, .FIllED is for filling the color to the circle

#cap =cv2.VideoCapture(0) used in main function

# mpHands =mp.solutions.hands
# hands = mpHands.Hands() #this object/class only uses RGB images so on the 13th line we have changed its type to rgb
# mpDraw = mp.solutions.drawing_utils

# pTime =0
# cTime =0


# while True:
#     success,img=cap.read()
#     imgRGB =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     results = hands.process(imgRGB)
    
#     # for multiple hands
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             for handLms in results.multi_hand_landmarks:
#                 # here lm ois called as landmakr which is considered here just a reference point of the tracing sings
#                 for id, lm in enumerate(handLms.landmark):
#                     # print(id,lm)
#                     h,w,c=img.shape # this wll give us width and height
#                     cx,cy = int(lm.x*w),int(lm.y*h) # this is the position of centre
#                     print(id,cx,cy) # the id nuber will help indexing he landmarks
#                     if id ==0: # is means no. of point in the image tracking points (Red points) 
#                         cv2.circle(img ,(cx,cy),15,(250,0,250),cv2.FILLED) # img is for image ,(cx,cy) is for the centre point of the image,(255,0,255) for color pink of circle, .FIllED is for filling the color to the circle
#                 mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # its is used to show the lines b/w the hand images.
    
#     cTime = time.time()  # it gives the current time

#     fps = 1/(cTime-pTime)# for megapixels it is created to calculate
#     pTime = cTime

#     cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)



#     cv2.imshow("image",img)
#     cv2.waitKey(1)

def main():
    pTime =0
    cTime =0
    cap =cv2.VideoCapture(0)
    detector=handDetector()


    while True:
        success,img=cap.read()
        img=detector.findHands(img)


        cTime = time.time()  # it gives the current time


        fps = 1/(cTime-pTime)# for megapixels it is created to calculate
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)



        cv2.imshow("image",img)
        cv2.waitKey(1)




if __name__=="__main__":
    main()