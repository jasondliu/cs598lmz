import weakref
import sys
import cv2
import numpy as np
import time

class Camera:
    def __init__(self, device, camera_id, resolution=(640, 480), fps=15):
        self.device = device
        self.name = 'Camera {}'.format(camera_id)
        self.camera_id = camera_id
        self.resolution = resolution
        self.fps = fps

    def get_resolution(self):
        return self.resolution

    def set_resolution(self, resolution):
        self.resolution = resolution

    def get_fps(self):
        return self.fps

    def set_fps(self, fps):
        self.fps = fps

    def set_camera_id(self, camera_id):
        self.camera_id = camera_id

    def get_camera_id(self):
        return self.camera_id

    def get_name(self):
        return self.name

    def _open(self):
        if self.camera_id == 'rtsp':
            self.cam = cv2.VideoCapture
