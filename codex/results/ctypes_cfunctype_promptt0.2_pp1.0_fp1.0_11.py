import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print 'called back with', value
    return value + 1

CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback2(value, value2):
    print 'called back with', value, value2
    return value + value2

CALLBACKFUNC3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback3(value, value2, value3):
    print 'called back with', value, value2, value3
    return value + value2 + value3

CALLBACKFUNC4 = ctypes.
