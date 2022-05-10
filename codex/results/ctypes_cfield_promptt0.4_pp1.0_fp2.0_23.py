import ctypes
# Test ctypes.CField object

import unittest
from test import test_support

import ctypes
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Test(unittest.TestCase):

    def test_offsetof(self):
        # offsetof() returns the offset of a field within a structure
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, sizeof(c_int))
        self.assertEqual(X.c.offset, sizeof(c_int) * 2)

    def test_sizeof(self):
        # sizeof()
