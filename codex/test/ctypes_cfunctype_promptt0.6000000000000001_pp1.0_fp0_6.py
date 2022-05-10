import ctypes
# Test ctypes.CFUNCTYPE, for functions with no arguments.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Prototype a function that takes no arguments
# and returns a simple integer
prototype = ctypes.CFUNCTYPE(ctypes.c_int)

# Get a pointer to the function
restype = ctypes.c_int
