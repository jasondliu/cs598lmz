import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Initialize SQLite
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

# Set SQLite functions
lib.sqlite3_open.argtypes = [ctypes.c_char_p,
                             ctypes.POINTER(ctypes.c_void_p)]
lib.sqlite3_open.restype = ctypes.c_int
lib.sqlite3_changes.argtypes = [ctypes.c_void_p]
lib.sqlite3_changes.restype = ctypes.c_int
lib.sqlite3_close.argtypes = [ctypes.c_void_p]
lib.sqlite3_close.restype = ctypes.c_int
lib.sqlite3_exec.argtypes = [ctypes.c_void_p,
                             ctypes.c_char_p,
                             ctypes.c_void_p,
                             ctypes.c_void_p,
                             ctypes.POINTER(ctypes.c_char_p)]
