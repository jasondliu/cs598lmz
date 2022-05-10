import ctypes
# Test ctypes.CField

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char)]
        self.assertEqual(ctypes.sizeof(X), 5)

    def test_offsetof(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char)]
        self.assertEqual(ctypes.sizeof(X.a), 4)
        self.assertEqual(ctypes.sizeof(X.b), 1)
        self.assertEqual(ctypes.addressof(X.a), ctypes.addressof(X()) + 0)
        self.assertEqual(ctypes.addressof(X.b), ctypes.addressof(X()) + 4)

    def test_from_address(self):

