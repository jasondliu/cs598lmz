import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# create the function
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

