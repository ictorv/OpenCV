import cv2
import imutils
import time

camera=cv2.VideoCapture(0)
time.sleep(1) #1 second delay to initilaise camera

StartFrame=None
area=500

while True:
    flag,img=camera.read()
    text="No Movement"
    img=imutils.resize(img, width=500)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(21,21),0)
    if StartFrame is None:
        StartFrame=blur
        continue
    differ=cv2.absdiff(StartFrame,blur)
    thresh=cv2.threshold(differ,25,255,cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh,None,iterations=2)
    contours=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(contours) #Grabbing every contours into single variable
    for con in contours:
        if cv2.contourArea(con)<area:
            continue
        (x,y,w,h)=cv2.boundingRect(con)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        text="Movement Found"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    cv2.imshow("CamCapt",img)
    key=cv2.waitKey(1) &0xFF
    if key == ord("x"):
        break

camera.release()
cv2.destroyAllWindows()



