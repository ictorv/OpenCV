
# Face Detection: Using Haar Cascade




## Module Installation
```pip install opencv```

## About Haar Cascade
An Algorithm for classification,here we have pre trained model which detect Eye, Nose and Mouth position and classify the image

[Model](https://github.com/opencv/opencv)

![Working Image](https://github.com/ictorv/OpenCV_Projects/blob/main/Face_Detection_using_Haar_Cascade/working.png)


#### Steps Followed:
> 1. Loading Algorithm 
```CascadeClassifier(algo)``` 

> 2. Initializing Camera
```cam=cv2.VideoCapture(0)```

> 3. Reading Frame from Camera
```flag,img=cam.read()```

> 4. Conversion of Color image image to Gray Scale Image
```gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)```

> 5. Obtaining Face Coordinate using Algorithm
```face=haar_cascade_mod.detectMultiScale(gray,1.3,4)```

> 6. Drawing Rectangle on Face
```cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)```

> 7. Displaying on Output Frame
```cv2.imshow("FaceDetection",img)```

For more Information Visit:
[Documentation](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

## Output

![Output](https://github.com/ictorv/OpenCV_Projects/blob/main/Face_Detection_using_Haar_Cascade/output.png)



