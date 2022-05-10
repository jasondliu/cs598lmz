import ctypes
# Test ctypes.CFUNCTYPE with a function returning a struct.
from ctypes import *
from ctypes.test import need_symbol
import unittest

class X(Structure):
    _fields_ = [("a", c_int)]

class CFUNCTYPE_TestCase(unittest.TestCase):
    def test_struct_return(self):
        f = CFUNCTYPE(X, c_int)(lambda arg: arg)
        x = f(42)
        self.assertEqual(x.a, 42)

    def test_struct_return_void_p(self):
        # This test assumes that the struct can be passed as an
        # argument to a function, and then returned as a result.
        # This is true for all platforms I know.
        f = CFUNCTYPE(X, POINTER(X))(lambda p: p[0])
        x = X(42)
        y = f(pointer(x))
        self.assertEqual(y.a, 42)

    def test_struct_return_pointer_to_struct(self):

