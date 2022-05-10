import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

# Use the system libc
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Set the memory allocators
libc.malloc.restype = ctypes.c_void_p
libc.malloc.argtypes = [ctypes.c_size_t]
libc.free.argtypes = [ctypes.c_void_p]

# Set the memory allocators
libc.malloc.restype = ctypes.c_void_p
libc.malloc.argtypes = [ctypes.c_size_t]
libc.free.argtypes = [ctypes.c_void_p]

# Set the threading functions
libc.pthread_create.restype = ctypes.c_int
libc.pthread_create.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
libc.pthread_join.restype = ctypes
