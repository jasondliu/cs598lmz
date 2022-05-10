import ctypes
# Test ctypes.CField.

import ctypes
import unittest

class TestCField(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1].offset, 0)

    def test_simple_2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1].offset, 0)
        self.assertEqual(X._fields_[1][1].offset, ctypes.sizeof(ctypes.c_int))

    def test_simple_3(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int), ("c", ctypes.c_int)]
        self.assertEqual(X._fields_
