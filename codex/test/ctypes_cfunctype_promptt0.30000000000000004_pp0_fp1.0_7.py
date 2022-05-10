import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A function taking a function pointer as argument
# and calling it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, CALLBACK)

