import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

# the function pointer type is defined in the C source file
# as:
# int (*func)(int)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print("func called with", n)
    return n + 1

