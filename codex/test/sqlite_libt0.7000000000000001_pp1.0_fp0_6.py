import ctypes
import ctypes.util
import threading
import sqlite3
import time
import re
import sys
import signal

class NSCamera(object):

    def __init__(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library('nscamera'))
        self.lib.initialize.restype = ctypes.c_void_p
        self.open_camera = self.lib.open_camera
        self.open_camera.restype = ctypes.c_bool
        self.open_camera.argtypes = [ctypes.c_void_p]
        self.close_camera = self.lib.close_camera
        self.close_camera.restype = None
        self.close_camera.argtypes = [ctypes.c_void_p]
        self.capture = self.lib.capture
        self.capture.restype = ctypes.c_bool
        self.capture.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
        self.update_camera_properties = self.lib
