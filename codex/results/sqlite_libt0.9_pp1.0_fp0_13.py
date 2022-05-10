import ctypes
import ctypes.util
import threading
import sqlite3
import queue
import datetime
import time

class libgphoto2():
    def __init__(self):
        self.libgphoto2 = self.load_library()
        self.gp_context = ctypes.pointer(ctypes.c_void_p())
        success = self.libgphoto2.gp_context_new(self.gp_context)
        self.camera = ctypes.pointer(ctypes.c_void_p())
        self.gp_port_info_list = ctypes.pointer(ctypes.c_void_p())
        self.gp_abilities_list = ctypes.pointer(ctypes.c_void_p())

    def __del__(self):
        if self.gp_context is not None:
            self.libgphoto2.gp_context_unref(self.gp_context)
        if self.camera is not None:
            self.libgphoto2.gp_camera_free(self.camera)

    def load_library(self):
        lib = ctypes.util.find_library("gphoto2")
