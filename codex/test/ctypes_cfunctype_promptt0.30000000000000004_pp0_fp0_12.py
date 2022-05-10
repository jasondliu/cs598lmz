import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX: This test is not complete, it only tests the basic
# functionality.

# a function
def func(x):
    return x * 2

# a function pointer type
CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call the function pointer
