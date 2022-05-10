import ctypes
ctypes.cdll.LoadLibrary('libSM.so')
ctypes.cdll.LoadLibrary('libICE.so')
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import numpy as np

class Camera():
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def get_frame(self):
        ret, frame = self.capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x
