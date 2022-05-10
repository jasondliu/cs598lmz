import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import math

# This is the path to the library file for the DLL
# It is relative to the location of this script
lib = ctypes.util.find_library('./lib/libdynamixel_sdk.so')

# This is the type of data that the DLL function returns
# In this case, it is an int
restype = ctypes.c_int

# These are the argtypes for the DLL function
# In this case, there are two ints
argtypes = [ctypes.c_char_p, ctypes.c_int]

# This opens the DLL
# The DLL file must be in the same directory as this script
# or you must change the path above
dyn = ctypes.CDLL(lib)

# This loads the function from the DLL
# The name of the function is "foo"
dyn.dxl_initialize.restype = restype
dyn.dxl_initialize.argtypes = argtypes

# This calls the function in the DLL
# It passes
