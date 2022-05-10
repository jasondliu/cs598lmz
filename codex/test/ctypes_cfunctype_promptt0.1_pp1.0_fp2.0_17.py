import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type, it takes an integer argument
# and returns an integer.
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we want to call.
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

# Get a pointer to the function.
