import ctypes
# Test ctypes.CFUNCTYPE

# This test checks that we can use a CFUNCTYPE to declare a function that takes
# a function as an argument.

import _ctypes_test

try:
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
except AttributeError:
    raise ImportError("requires ctypes")


def func(a, b):
    return a + b

f = cfunc(func)
