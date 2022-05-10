import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a function with a simple argument and return type.
#

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

paramflags = (1, "x")

def func(*args):
    return args[0] * 2

