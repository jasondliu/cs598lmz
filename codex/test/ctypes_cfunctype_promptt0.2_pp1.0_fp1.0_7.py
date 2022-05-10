import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

# call a function
