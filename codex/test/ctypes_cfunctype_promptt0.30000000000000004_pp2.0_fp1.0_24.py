import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this is a function which takes a function pointer as argument,
# and calls the function.

# The function takes an integer argument, and returns an integer.
# The function pointer argument must have the same signature.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with argument", arg)
    return arg + 42

CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback2(arg1, arg2):
    print("callback2 called with arguments", arg1, arg2)
    return arg1 + arg2 + 42

