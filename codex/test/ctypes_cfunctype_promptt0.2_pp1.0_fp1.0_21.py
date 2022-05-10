import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a simple function that takes a pointer to a function
# as an argument, and calls the function.

# The function takes an integer argument, and returns an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

