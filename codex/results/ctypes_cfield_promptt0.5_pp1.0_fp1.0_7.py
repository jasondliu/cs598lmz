import ctypes
# Test ctypes.CField

# This test is meant to be run on a 32 bit platform.

import ctypes
import unittest
from ctypes import *

class CFieldTestCase(unittest.TestCase):
    def test_field_simple(self):
        class X(Structure):
            _fields_ = [("a", c_int),
                        ("b", c_int),
                        ("c", c_int)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, sizeof(c_int))
        self.assertEqual(X.c.offset, sizeof(c_int) * 2)

    def test_field_bit(self):
        class X(Structure):
            _fields_ = [("a", c_int, 4),
                        ("b", c_int, 4),
                        ("c", c_int, 4)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 0)
        self.assertEqual(X.
