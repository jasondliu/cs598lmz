import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os

# Load the library.
lib = ctypes.CDLL(ctypes.util.find_library('c'))

# Set up the prototype and parameters for the function call.
lib.malloc.restype = ctypes.c_void_p
lib.malloc.argtypes = (ctypes.c_size_t,)

# Call the function.
buf = lib.malloc(1024)

# Convert the returned pointer to a Python integer.
print "Address of buffer:", ctypes.addressof(buf)

# Convert the returned pointer to a ctypes instance.
buf = ctypes.c_void_p(buf)

# Create a mutable string buffer.
buf = ctypes.create_string_buffer("Hello world", 1024)

# Create a mutable string buffer.
buf = ctypes.create_string_buffer(1024)

# Create a mutable string buffer.
buf = ctypes.create_string_buffer(1024)

# Create a mutable string buffer.
buf = ctypes.create_string_
