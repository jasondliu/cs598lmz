import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument.
# The function pointed to must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CMPFUNC
def func(arg):
    print("func", arg)
    return arg

