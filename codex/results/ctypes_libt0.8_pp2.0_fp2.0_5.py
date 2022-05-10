import ctypes
ctypes.CDLL("C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\14.0\\VC\\redist\\x86\\Microsoft.VC141.CRT\\opencv_world310.dll")

import os
import cv2
import numpy as np
from keras.models import load_model

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self, model):
        
        _, frame = self.video.read()

        # mirror the frame
        frame = cv2.flip(frame, 1)

        # video resolution
        vid_w, vid_h = frame.shape[1], frame.shape[0]

        # basic image segmentation
        # resize it
        frame_resized = cv2.resize(frame, (64, 64))

        # grayscale it
        frame_gr
