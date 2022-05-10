import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be called by the callback function.
# It takes an integer argument and returns an integer.

def py_callback(arg):
    print("py_callback called with %d" % arg)
    return arg * 2

# This is the callback function.  It calls the Python function
# py_callback.

def callback(arg):
    print("callback called with %d" % arg)
    return py_callback(arg)

# This is the function that takes a function pointer as argument.
# It calls the callback function.

def func(callback):
    print("func called with %x" % callback)
    return callback(42)

# This is the function
