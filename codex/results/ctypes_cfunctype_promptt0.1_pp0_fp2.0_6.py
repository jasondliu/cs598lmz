import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this is a function that takes a function pointer as argument
# and calls it.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback2(arg1, arg2):
    print("callback2 called with arguments", arg1, arg2)
    return arg1 + arg2

# call the function with a python callable
res = lib.call_function(CALLBACKFUNC(callback), 1)
if res != 2:
    raise Exception("wrong result")

res = lib.call_function(CALLBACKFUNC2(callback2), 1, 2)
