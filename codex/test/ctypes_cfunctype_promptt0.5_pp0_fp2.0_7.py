import ctypes
# Test ctypes.CFUNCTYPE

# This is a simple test to see if ctypes.CFUNCTYPE works with
# functions returning a structure by value.

from ctypes import *
import unittest

class TestCFUNCTYPE(unittest.TestCase):
    def test_simple(self):
        class X(Structure):
            _fields_ = [("a", c_int)]

        x = X(1)

        Xp = POINTER(X)
        f = CFUNCTYPE(X)(lambda: x)
        self.assertEqual(f(), x)
        self.assertEqual(f().a, x.a)

    def test_simple_p(self):
        class X(Structure):
            _fields_ = [("a", c_int)]

        x = X(1)

        Xp = POINTER(X)
        f = CFUNCTYPE(Xp)(lambda: pointer(x))
        self.assertEqual(f().contents, x)
