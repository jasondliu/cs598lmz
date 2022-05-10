import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)

    def test_simple_with_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1)]
        self.assertEqual(X.a.offset, 1)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)

    def test_simple_with_offset_and_size(self):
        class X(ctypes.Structure):
            _fields
