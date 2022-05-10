import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is called with a function pointer as first argument.
# The function pointer is called with an integer argument, and should
# return an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print('callback called with', value)
    return value + 1

CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback2(value, value2):
    print('callback2 called with', value, value2)
    return value + value2

CALLBACKFUNC3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

