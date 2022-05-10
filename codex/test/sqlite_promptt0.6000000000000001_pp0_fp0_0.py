import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('path/to/database').cursor().execute('select * from table')

import sys
import os

# ==========
# = Logger =
# ==========

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

sys.stdout = Logger("/var/log/pi-face-recognition.log")

# ===============
# = PiCamera API =
# ===============

class PiCamera(object):
    def __init__(self):
        self.camera = ctypes.cdll.LoadLibrary(ctypes.util.find_library('mmal_core'))
        self.camera.mmal_component_create.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32)]
        self.camera.mm
