import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is defined in _ctypes_test.c
# It takes a function pointer as first argument, and calls
# this function with the other arguments.

CALLFUNC = lib._testfunc_callback
CALLFUNC.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int, ctypes.c_int)
CALLFUNC.restype = ctypes.c_int

# This is the function to be called.  It returns the sum of its
# arguments.

def func(a, b):
    return a + b

# This is the function type the callback must have.  The arguments
# are all c_int, the return type is c_int too.

CFUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create the callback function

