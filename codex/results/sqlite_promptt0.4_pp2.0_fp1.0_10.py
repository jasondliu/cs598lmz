import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import time

import logging
log = logging.getLogger(__name__)

lib = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

lib.memset.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_size_t,
]

lib.memset.restype = ctypes.c_void_p

lib.memcpy.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
]

lib.memcpy.restype = ctypes.c_void_p

lib.memcmp.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
]

lib.memcmp.restype = ctypes.c_int

lib.strlen.argtypes = [
