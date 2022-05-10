import ctypes
import ctypes.util
import threading
import sqlite3

from . import utils

# By default, use the system-wide sqlite3 library.
sqlite3_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

# Set up the return types for the sqlite3 library functions.
sqlite3_lib.sqlite3_open.restype = ctypes.c_int
sqlite3_lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite3_lib.sqlite3_close.argtypes = [ctypes.c_void_p]
sqlite3_lib.sqlite3_close.restype = ctypes.c_int
sqlite3_lib.sqlite3_exec.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)]
sqlite3_lib.sqlite3
