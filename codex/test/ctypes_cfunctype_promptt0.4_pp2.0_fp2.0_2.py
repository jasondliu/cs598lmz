import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple function

def func(arg):
    "A simple function"
    return arg + 1

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call the function with a ctypes callback

