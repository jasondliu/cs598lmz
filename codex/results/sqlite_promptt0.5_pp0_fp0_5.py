import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import pdb

# Define the type for the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

# Define the type for the callback function
CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

# Define the type for the callback function
CALLBACKFUNC3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)

# Define the type for the callback function
CALLBACKFUNC4 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)

# Define the type for the callback function
CALLBACKFUNC5 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes
