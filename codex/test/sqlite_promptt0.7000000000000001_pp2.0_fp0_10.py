import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").execute("SELECT sqlite_version()").fetchone()[0]

import pyfastnoisesimd as fns
import numpy as np

# lib is here
lib_path = ctypes.util.find_library("libpyfastnoisesimd.so")
lib = ctypes.CDLL(lib_path)

# this is the function we want to call
lib.FNS_GetNoiseSet.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.FNS_GetNoiseSet.restype = ctypes.POINTER(ctypes.c_float)

lib.FNS_SetNoiseType.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib
