import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple function

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

paramflags = (1, "x")

restype = ctypes.c_int

argtypes = (ctypes.c_int,)

functype = ctypes.CFUNCTYPE(restype, *argtypes)

