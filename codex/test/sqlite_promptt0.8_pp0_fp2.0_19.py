import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
con = sqlite3.connect(':memory:')

camera = cv2.VideoCapture(0)
ret = camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
ret = camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Stabilizing the camera
for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite("opencv" + str(i) + ".png", image)
    del(camera)

# Test webcam again
camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite("opencv_test_again.png", image)
del(camera)

# Test classifier
haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_faces(f_cascade, colored_img, scaleFactor = 1.1):
    img_copy = colored_img.copy()
   
