## Module Installation
```pip install imutils```<br>
```pip install opencv-python```

## Steps:
1. Reading Frame from Camera
>```flag,frame=cam.read()```
2. Preprocessing of image
> a. Resizing<br>
> b. Blurring<br>
> c. Masking<br>
> d. Erosion<br>
> e. Dilation<br>
3. Finding contours
> ```cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]```
4. Drawing Minimum enclosing circle
> ```c=max(cnts,key=cv2.contourArea)```
  ```((x,y),radius)=cv2.minEnclosingCircle(c)```
4. Finding centre of contour area
> ```M=cv2.moments(c)```<br>
 ```center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))```
5. Drawing Circle and centre
> ```cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)```
    ```cv2.circle(frame,center,5,(0,0,255),-1)```
6. Direction using radius and position
