import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of the ctypes.CFUNCTYPE type.
#
# The test is based on the example in the ctypes documentation:
# http://docs.python.org/library/ctypes.html#function-prototypes

import unittest
from test import test_support

# The following is a C function declaration:
#
# int add(int a, int b) {
#     return a + b;
# }
#
# The following is the equivalent Python code:

import ctypes

libc = ctypes.CDLL(None)

c_int_p = ctypes.POINTER(ctypes.c_int)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Z(ct
