{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "dedac691",
   "metadata": {},
   "source": [
    "\n",
    "# <center><span style=\"font-family:cursive;\">Face Detection: Using Haar Cascade</span></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8f7fa23",
   "metadata": {},
   "source": [
    "<div style=\"color:white;\n",
    "           display:fill;\n",
    "           border-radius:5px;\n",
    "           background-color:lightblue;\n",
    "           font-size:110%;\n",
    "           font-family:Verdana;\n",
    "           letter-spacing:0.5px\">\n",
    "\n",
    "<p style=\"padding: 15px; color:white; text-align:center\"><b>Module Installation</b></p>\n",
    "</div>\n",
    "\n",
    ">```pip install opencv```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0ea5ad1",
   "metadata": {},
   "source": [
    "<div style=\"color:white;\n",
    "           display:fill;\n",
    "           border-radius:5px;\n",
    "           background-color:lightblue;\n",
    "           font-size:110%;\n",
    "           font-family:Verdana;\n",
    "           letter-spacing:0.5px\">\n",
    "\n",
    "<p style=\"padding: 15px; color:white; text-align:center\"><b>About Haar Cascade</b></p>\n",
    "</div>\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7cc38166",
   "metadata": {},
   "source": [
    "<img src=\"haar%20cascade%20face.png\"  width=\"300\" height=\"150\">\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc6163dc",
   "metadata": {},
   "source": [
    "\n",
    "<p>Here we have pre trained model which detect Eye, Nose and Mouth position and classify the image</p>\n",
    "\n",
    "##### Model : <a href=\"https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml\" target=\"_blank\">Haar Cascade</a>\n",
    "\n",
    "### Steps Followed:\n",
    "> 1.Loading Algorithm <br>\n",
    "```CascadeClassifier(algo)``` <br>\n",
    "\n",
    "> 2.Initializing Camera<br>\n",
    "```cam=cv2.VideoCapture(0)```<br>\n",
    "\n",
    "> 3.Reading Frame from Camera<br>\n",
    "```flag,img=cam.read()```<br>\n",
    "\n",
    "> 4.Conversion of Color image image to Gray Scale Image<br>\n",
    "```gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)```<br>\n",
    "\n",
    "> 5.Obtaining Face Coordinate using Algorithm<br>\n",
    "```face=haar_cascade_mod.detectMultiScale(gray,1.3,4)```<br>\n",
    "\n",
    "> 6.Drawing Rectangle on Face<br>\n",
    "```cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)```<br>\n",
    "\n",
    "> 7.Displaying on Output Frame<br>\n",
    "```cv2.imshow(\"FaceDetection\",img)```<br>\n",
    "\n",
    "For more Information Visit:\n",
    "##### <a href=\"https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html\" target=\"_blank\">Documentation</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24f1e2a3",
   "metadata": {},
   "source": [
    "<div style=\"color:white;\n",
    "           display:fill;\n",
    "           border-radius:5px;\n",
    "           background-color:lightblue;\n",
    "           font-size:110%;\n",
    "           font-family:Verdana; \n",
    "           letter-spacing:0.5px\">\n",
    "\n",
    "<p style=\"padding: 15px; color:white; text-align:center\"><b>Output</b></p>\n",
    "</div>\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "4d59740d",
   "metadata": {},
   "source": [
    "<img src=\"output.png\"  width=\"300\" height=\"150\">\n",
    "Press "
   ]
  },
  {
   "cell_type": "raw",
   "id": "def56312",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
