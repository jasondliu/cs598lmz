import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("vpc.db")
import traceback
import binascii
import logging
import os
import hashlib

# for ctypes
class c_void(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

class c_char_p(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_char * 1)]

if sys.platform == "darwin":
    libvpc = ctypes.cdll.LoadLibrary("libvpc.dylib")
elif sys.platform == "windows":
    libvpc = ctypes.cdll.LoadLibrary("libvpc-3.dll")
else:
    libvpc = ctypes.cdll.LoadLibrary("libvpc.so")

# for ctypes
class vpc_string(ctypes.Structure):
    _fields_ = [("str", ctypes.c_char_p),("len", ctypes.c_int)]

class vpc_file(ctypes.Structure):
    _fields_ = [
