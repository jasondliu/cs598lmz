import ctypes
import ctypes.util
import threading
import sqlite3
import os

# Get the location of the sqlite3 library.
sqlite3_lib = ctypes.util.find_library('sqlite3')

# Load the library.
sqlite3 = ctypes.CDLL(sqlite3_lib)

# Set the types of the arguments.
sqlite3.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite3.sqlite3_exec.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)]

# Set the return types.
sqlite3.sqlite3_open.restype = ctypes.c_int
sqlite3.sqlite3_exec.restype = ctypes.c_int

# Create a new database.
db = ctypes.c_void_p()
