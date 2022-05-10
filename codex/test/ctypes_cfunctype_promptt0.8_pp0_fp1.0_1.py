import ctypes
# Test ctypes.CFUNCTYPE(...)

from ctypes import *
from ctypes.util import find_library

# Load the C library
lib = cdll.LoadLibrary(find_library("m") or "libm.dylib")

# Define argument and return types
sin_func = CFUNCTYPE(c_double, c_double)(("sin", lib), ((1, "x"),))

print("sin(1.0) =", sin_func(1.0))
