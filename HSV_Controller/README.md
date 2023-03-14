# HSV Controller
HSV Function<br>
```hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)```

TrackBar <br>
Naming
```cv2.namedWindow("HSV_Window")```<br>

Creating
```cv2.createTrackbar('L-Hue',"HSV_Window",0,179, passing)```

Controller eg.
```low_h= cv2.getTrackbarPos('L-Hue',"HSV_Window")``` 