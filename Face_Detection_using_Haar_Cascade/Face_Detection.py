import cv2
algo="haarcascade_face.xml" #accessing model file
haar_cascade_mod=cv2.CascadeClassifier(algo) #passing trained algorithm

cam=cv2.VideoCapture(0)
while True:
    text="No Human Face"
    flag,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face=haar_cascade_mod.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        text="Human Face"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    cv2.imshow("Face Detection",img)
    key=cv2.waitKey(1) &0xFF
    if key == ord("x"):
        break
cam.release()
cv2.destroyAllWindows()

#Press x to Close

