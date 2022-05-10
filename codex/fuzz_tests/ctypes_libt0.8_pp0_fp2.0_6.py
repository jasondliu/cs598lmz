import ctypes
ctypes.CDLL('./kinect.so').kinect_init()
import time

import numpy as np 
import cv2

from ctypes import *
import datetime

def get_image():
    ctypes.CDLL('./kinect.so').kinect_init()
    ctypes.CDLL('./kinect.so').get_image()
    ctypes.CDLL('./kinect.so').stop_transfer()
    im = np.load('image.npy')
    return im

def get_depth():
    ctypes.CDLL('./kinect.so').kinect_init()
    ctypes.CDLL('./kinect.so').get_depth()
    ctypes.CDLL('./kinect.so').stop_transfer()
    im = np.load('depth.npy')
    return im

if __name__ == '__main__':
    im = get_image()
    cv2.imshow('kk', im)
    cv2.waitKey(0)
    im = get
