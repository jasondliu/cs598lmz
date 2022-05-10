import ctypes
# Test ctypes.CField

import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):
    def test_field_offset(self):
        # Check that the offset of a field is correct.
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(ctypes.c_int),
                         ctypes.sizeof(X.a))
        self.assertEqual(ctypes.sizeof(ctypes.c_int),
                         ctypes.sizeof(X.b))
        self.assertEqual(0, X.a.offset)
        self.assertEqual(ctypes.sizeof(ctypes.c_int), X.b.offset)

    def test_field_size(self):
        # Check that the size of a field is correct.
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("
