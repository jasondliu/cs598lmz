import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

CALLBACKFUNC.restype = ctypes.c_int
CALLBACKFUNC.argtypes = (ctypes.c_int,)

# This is the function that takes a function pointer as argument
# and calls it.

