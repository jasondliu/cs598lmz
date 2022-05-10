import ctypes
import ctypes.util
import threading
import sqlite3

import cv2
import numpy as np

from . import camera


class Camera(camera.Camera):

    def __init__(self, camera_id, resolution, fps, device_id=None,
                 device_serial=None, device_name=None, device_type=None,
                 device_model=None, device_vendor=None, device_version=None,
                 device_info=None):
        super(Camera, self).__init__(camera_id, resolution, fps)

        self.device_id = device_id
        self.device_serial = device_serial
        self.device_name = device_name
        self.device_type = device_type
        self.device_model = device_model
        self.device_vendor = device_vendor
        self.device_version = device_version
        self.device_info = device_info

        self.camera = None
        self.capture = None
        self.capture_thread = None
        self.capture_thread_lock = threading.RLock()

        self.
