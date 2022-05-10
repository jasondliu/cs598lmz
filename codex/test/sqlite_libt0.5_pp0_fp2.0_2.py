import ctypes
import ctypes.util
import threading
import sqlite3
import os

from sys import platform

# Import the correct library for the platform
if platform == "darwin":
    lib = ctypes.cdll.LoadLibrary("./libpyzm.dylib")
elif platform == "linux" or platform == "linux2":
    lib = ctypes.cdll.LoadLibrary("./libpyzm.so")
else:
    raise Exception("Platform not supported")

# Define the types of the C functions we want to use
lib.ZM_LoadDB.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.ZM_LoadDB.restype = ctypes.c_int
lib.ZM_CloseDB.argtypes = [ctypes.c_char_p]
lib.ZM_CloseDB.restype = ctypes.c_int
lib.ZM_GetZone.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.ZM_GetZone.restype = ctypes.c_char_p
lib
