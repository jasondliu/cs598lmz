import ctypes
# Test ctypes.CField

import ctypes
import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X._fields_[0].name, "a")
        self.assertEqual(X._fields_[0].type, ctypes.c_int)
        self.assertEqual(X._fields_[0].offset, 0)

    def test_simple_with_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int, 1)])
        self.assertEqual(X._fields_[0].name, "a")
        self.assertEqual(X._fields
