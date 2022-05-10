import ctypes
import ctypes.util
import threading
import sqlite3
import time

start_time=time.time()

# Import the Google cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#define lib name
libname = ctypes.util.find_library("sense_hat")

try:
    lib = ctypes.CDLL(libname)
except OSError:
    print("No sense hat")

    class SenseHat:
        def clear(self):
            pass
else: # Sense hat found
    #clear
    lib.clear.argtypes = []
    lib.clear.restype = None

    #set pixel
    lib.set_pixel.argtypes = [ ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 ]
    lib.set_pixel.restype = None

    #get pixel
    lib.get_pixel.argtypes = [ ctypes.c_uint8, ctypes.c_uint8 ]
    lib.get_pixel.restype =
