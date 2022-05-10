import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a simple argument
# and a simple result

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

