import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Test with a function with a simple result type

# int function(int)
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

