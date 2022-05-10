import ctypes
ctypes.cdll.LoadLibrary('/usr/local/opt/opencv/lib/python2.7/site-packages/cv2.so')

import cv2

#Import sys libraries
import sys
import time

#Import Camera module
from camera import Camera

#Import numpy
import numpy as np

def main(argv):
    cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    camera = Camera()
    camera.set_resolution(0, 720, 480) #320x240 is the default resolution

    camera.preview(True)
    time.sleep(1)

    camera.start_recording(time.strftime("%Y-%m-%d %H:%M:%S") + ".h264")
    time.sleep(120)

    camera.stop_recording
