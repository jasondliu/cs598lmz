import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import cv2
import sys
import numpy as np

class FaceDetector:
    def __init__(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library('libfacedetection'))
        self.lib.facedetection_init()
        self.lib.facedetection_set_min_size(20)
        self.lib.facedetection_set_threshold(0.3)
        self.lib.facedetection_set_scale_factor(1.2)
        self.lib.facedetection_set_max_size(1000)
        self.lib.facedetection_set_max_num_detections(10)
        self.lib.facedetection_set_max_num_threads(4)
        self.lib.facedetection_set_num_trees(10)
        self.lib.facedetection_set_num_features(13)
        self.lib.facedetection_set_num_levels(5)
