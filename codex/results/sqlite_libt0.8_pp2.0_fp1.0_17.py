import ctypes
import ctypes.util
import threading
import sqlite3
import atexit
import os
import ctypes
import ctypes.util

# Create instance of libc
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Set up the prototype and parameters
libc.srandom(ctypes.c_ulong(0))
libc.random.restype = ctypes.c_long

# Call the function
libc.random()

# libc.srand(ctypes.c_ulong(0))
# libc.rand.restype = ctypes.c_long
# libc.rand()
