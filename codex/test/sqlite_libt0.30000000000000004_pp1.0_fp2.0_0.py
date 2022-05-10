import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime

# This is a hack to get the path of the library
# TODO: Find a better way to do this
if sys.platform == 'darwin':
    lib_path = os.path.join(os.path.dirname(__file__), 'lib', 'libgps.dylib')
else:
    lib_path = os.path.join(os.path.dirname(__file__), 'lib', 'libgps.so')

libgps = ctypes.CDLL(lib_path)

# Callback types
callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

# GPSD types
