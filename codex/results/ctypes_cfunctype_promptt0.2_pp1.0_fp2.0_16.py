import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# this is a function that takes a function pointer as argument
# and calls it

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print "callback", value
    return value + 1

CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback2(value, value2):
    print "callback2", value, value2
    return value + value2

# this function takes a function pointer as argument, and calls it
# with a value

lib.callit.argtypes = (CALLBACKFUNC, ctypes.c_int)
lib.callit.restype = ctypes.c_int

lib.callit2.argtypes = (CALLBACKFUNC2, ctypes.c_int, ctypes.c_
