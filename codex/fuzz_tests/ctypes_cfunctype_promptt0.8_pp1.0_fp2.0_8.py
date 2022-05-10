import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.test import need_symbol
from ctypes.test.test_pickling import *
import sys
import _ctypes_test

CDataType = type(c_int())

libc = CDLL("libc.so.6")


class X(Structure):
    _fields_ = [("a", c_int)]


class Y(Structure):
    _fields_ = [("p", POINTER(X))]


class Z(Structure):
    _fields_ = [("y", Y)]


class my_test(unittest.TestCase):
    def test_1(self):
        # Call a function of the form
        #   int func(int, int)
        proto = CFUNCTYPE(c_int, c_int, c_int)
        func = proto((("funcname", libc), (1, "first"), (1, "second")))
        result = func(2, 3)
        self.assertEqual(result, 2+3)

    def test_2(
