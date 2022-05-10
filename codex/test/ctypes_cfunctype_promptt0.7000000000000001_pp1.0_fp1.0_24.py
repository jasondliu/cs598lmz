import ctypes
# Test ctypes.CFUNCTYPE

# This unittest is for ctypes.CFUNCTYPE.
#
# The C code:
#
# #include <stdio.h>
#
# typedef int (*PF)(int);
#
# int test(PF pf) {
#    return pf(2) + pf(3);
# }
#
# The Python code:
#
# from ctypes import *
#
# def func(x):
#    return x * x
#
# pf = CFUNCTYPE(c_int, c_int)(func)
#
# lib.test.restype = c_int
#
# print lib.test(pf)

from ctypes import *

try:
    import _ctypes_test
except ImportError:
    import sys
    if sys.platform == "win32":
        raise unittest.SkipTest("Need _ctypes_test.dll")
    else:
        raise unittest.SkipTest("Need _ctypes_test.so")

