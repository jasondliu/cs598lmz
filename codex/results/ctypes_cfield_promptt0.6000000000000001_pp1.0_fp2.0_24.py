import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X(10).a, 10)

    def test_nested(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        class Y(ctypes.Structure):
            _fields_ = [("x", X)]
        self.assertEqual(ctypes.sizeof(Y), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(Y(X(10)).x.a, 10)

    def test_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
