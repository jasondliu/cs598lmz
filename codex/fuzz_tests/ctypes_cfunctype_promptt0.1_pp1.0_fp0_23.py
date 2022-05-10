import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that we pass to the dll.

def callback(i):
    print("callback", i)
    return i + 1

# This is the function that calls the dll function.

def callit(func):
    lib.set_callback(CALLBACKFUNC(func))
    res = lib.call_callback(3)
    print("result", res)

callit(callback)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# a pointer to a function that takes an integer argument and
# returns an integer.

CALLBACKFUNC2 = ctypes.CFUNCTYPE(
