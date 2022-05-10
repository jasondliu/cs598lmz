import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to be passed as argument.

def callback(value):
    print("callback called with", value)
    return value + 1

# This is the function that takes the function pointer.

lib.pass_function(CALLBACKFUNC(callback))

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# a pointer to a function.

CALLBACKFUNC2 = ctypes.CFUNCTYPE(CALLBACKFUNC, ctypes.c_int)

# This is the function to be passed as argument.

def callback2(value):
    print("callback2 called with",
