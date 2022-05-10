import ctypes
# Test ctypes.CField instance
import sys
from ctypes import *
import unittest
from test import test_support

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("y", c_int),
                ("c", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int),
                ("d", c_int)]

class TestCField(unittest.TestCase):
    def test_offset(self):
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, sizeof(c_int))

        self.assertEqual(Y.a.offset, 0)
        self.assertEqual(Y.b.offset, sizeof(c_int))
        self.assertEqual(Y.
