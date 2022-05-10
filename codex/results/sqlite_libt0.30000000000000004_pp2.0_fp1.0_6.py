import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import math
import struct
import traceback
import binascii
import random
import string
import logging
import logging.handlers
import argparse

# import the shared library
lib = ctypes.CDLL(ctypes.util.find_library('libc'))

# define the restype and argtypes
lib.malloc.restype = ctypes.c_void_p
lib.malloc.argtypes = (ctypes.c_size_t,)
lib.free.argtypes = (ctypes.c_void_p,)

# define the callback type
CALLBACK_TYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

# define the callback
def callback(a, b, c, d, e, f):
    print("callback:", a, b, c, d, e, f)
    return 0

# create the callback
