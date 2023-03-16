from facial_emotion_recognition import EmotionRecognition
import cv2
recog=EmotionRecognition(device='cpu')

cam=cv2.VideoCapture(0)

while True:
    flag,frame=cam.read()
    frame=recog.recognise_emotion(frame,return_type="BGR")
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1) 
    if key==27:
        break

cam.release()
cv2.destroyAllWindows()
