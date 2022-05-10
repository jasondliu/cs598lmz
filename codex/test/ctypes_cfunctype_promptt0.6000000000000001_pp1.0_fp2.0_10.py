import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(x):
    return x * 2

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# convert the Python function into a C function pointer
cfunc = CALLBACKFUNC(func)

# pass the function pointer to a C callback function
