import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the following signature:
# int func(double)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

# This is the function to pass to the callback function.
