import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Prototype a function with two int arguments and returning an int
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create a new function with prototype
restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)
