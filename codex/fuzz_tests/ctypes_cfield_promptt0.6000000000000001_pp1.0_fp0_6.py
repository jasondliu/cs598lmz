import ctypes
# Test ctypes.CField implementation.

from ctypes import *
import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_field(self):
        class X(Structure):
            _fields_ = [("a", c_int),
                        ("b", c_int),
                        ("c", c_int)]

        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, 0)
        self.assertEqual(x.c, 0)

        x.a = 1
        x.b = 2
        x.c = 3
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 2)
        self.assertEqual(x.c, 3)

    def test_getattr(self):
        class X(Structure):
            _fields_ = [("a", c_int),
                        ("b", c_int),
                        ("c", c_int)]

        x = X()
        self.assertRa
