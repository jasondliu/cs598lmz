import ctypes
# Test ctypes.CField

# This test is not complete.  It only tests the functionality that
# is currently used by the ctypes implementation.

import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):
    def test_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(ctypes.c_int), X.a.offset)
        self.assertEqual(2 * ctypes.sizeof(ctypes.c_int), X.b.offset)

    def test_size(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(ctypes.c_int), X.a.size)
        self.assertEqual(ctypes.sizeof(ctypes.c_int
