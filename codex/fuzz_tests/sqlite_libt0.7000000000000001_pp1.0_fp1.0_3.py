import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import struct
import shutil
import re
import sys
import os
import time

# Load libxdo.so
try:
    libxdo = ctypes.cdll.LoadLibrary('libxdo.so')
except:
    print 'Unable to find libxdo.so in the LD_LIBRARY_PATH'
    exit()

# Declare function arguments for libxdo.so
libxdo.xdo_new.argtypes = [ctypes.c_char_p]
libxdo.xdo_new.restype = ctypes.POINTER(ctypes.c_int)

libxdo.xdo_free.argtypes = [ctypes.POINTER(ctypes.c_int)]
libxdo.xdo_free.restype = None

libxdo.xdo_click.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
libxdo.xdo_click.restype = ctypes.c_int

lib
