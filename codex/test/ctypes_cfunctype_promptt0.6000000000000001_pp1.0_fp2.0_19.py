import ctypes
# Test ctypes.CFUNCTYPE(...)(func)

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(arg):
    return arg + 3

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

