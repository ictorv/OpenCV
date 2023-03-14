import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow("HSV_Window")

def passing(x):
	pass

cv2.createTrackbar('L-Hue',"HSV_Window",0,179, passing)
cv2.createTrackbar('L-Saturation',"HSV_Window",0,255, passing)
cv2.createTrackbar('L-Value',"HSV_Window",0,255, passing)
cv2.createTrackbar('H-Hue',"HSV_Window",0,179, passing)
cv2.createTrackbar('H-Saturation',"HSV_Window",0,255, passing)
cv2.createTrackbar('H-Value',"HSV_Window",0,255, passing)

while True:
	flag,img=cap.read()
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	low_h= cv2.getTrackbarPos('L-Hue',"HSV_Window")
	low_s = cv2.getTrackbarPos('L-Saturation', "HSV_Window")
	low_v = cv2.getTrackbarPos('L-Value', "HSV_Window")
	high_h = cv2.getTrackbarPos('H-Hue', "HSV_Window")
	high_s = cv2.getTrackbarPos('H-Saturation', "HSV_Window")
	high_v = cv2.getTrackbarPos('H-Value', "HSV_Window")

	min=np.array([low_h,low_s,low_v])
	max = np.array([high_h, high_s, high_v])
	mask=cv2.inRange(hsv,min,max)

	result=cv2.bitwise_and(img,img,mask=mask)

	cv2.imshow("Capture",img)
	cv2.imshow("Mask", mask)
	cv2.imshow("Result", result)

	key=cv2.waitKey(1) & 0xFF
	if key ==ord("x"):
		break

img.release()
cv2.destroyAllWindows()
