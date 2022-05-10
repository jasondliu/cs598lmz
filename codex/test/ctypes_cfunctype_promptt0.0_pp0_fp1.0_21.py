import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The prototype of the function is:
# int callback(int (*func)(int))

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(arg):
    print("func() called with %d" % arg)
    return arg + 1

# The callback function is called by the C code.  It calls the
# function pointer we pass, and returns the result.

@CALLBACK
def callback(func):
    print("callback() called with %x" % func)
    return func(42)

# This is the function that calls the callback function.

