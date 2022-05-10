import socket
socket.if_indextoname(3)

##
import netifaces
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']

##
os.system('python3 face_detect.py')

##
# file = open("/home/pi/Desktop/test_opencv.txt","w")
# file.write("this is a test")
# file.close()

##
import time
start_time = time.time()

import cv2
face_cascade = cv2.CascadeClassifier("/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/pi/opencv/data/haarcascades/haarcascade_eye.xml")

webcam = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not webcam.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = webcam.read
