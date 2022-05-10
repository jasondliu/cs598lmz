import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Load the libraries
import cv2
import numpy as np
import pyautogui
import time
import os

# Initialize the variables

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

# To set the frame width and height
cap.set(3,1280)
cap.set(4,720)

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y),
