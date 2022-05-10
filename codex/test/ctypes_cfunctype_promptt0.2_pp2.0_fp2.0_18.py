import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX This test is not complete yet

# This is a function that takes a function pointer as an argument
# and calls it.
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback", value)
    return value + 1

# This is the function that calls the callback function.
