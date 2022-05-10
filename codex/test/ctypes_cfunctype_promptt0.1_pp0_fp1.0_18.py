import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the following signature:
# int func(double)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

# This is the function that will be passed to the C function.

def py_cmp_func(a):
    print("py_cmp_func called with", a)
    return -1

# This is the C function that takes a function pointer as argument.

