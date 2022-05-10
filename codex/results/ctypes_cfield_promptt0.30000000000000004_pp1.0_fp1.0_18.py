import ctypes
# Test ctypes.CField

# This is a test for ctypes.CField

import unittest
from ctypes import *

class CFieldTestCase(unittest.TestCase):

    def test_field_1(self):
        class X(Structure):
            _fields_ = [("a", c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, sizeof(c_int))

    def test_field_2(self):
        class X(Structure):
            _fields_ = [("a", c_int),
                        ("b", c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, sizeof(c_int))
        self.assertEqual(X.b.offset, sizeof(c_int))
        self.assertEqual(X.b.size, sizeof(c_int))

    def test_field_3(self):
        class X(Structure):
            _fields_ = [("a",
