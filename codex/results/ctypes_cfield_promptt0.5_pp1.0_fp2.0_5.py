import ctypes
# Test ctypes.CField.

import unittest
import sys

class CFieldTest(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]

        self.assertEqual(X._fields_[0][1], ctypes.c_int)

    def test_bitfield(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int, 1)]

        self.assertEqual(X._fields_[0][1], ctypes.c_int)
        self.assertEqual(X._fields_[0][2], 1)

    def test_bitfield_int_type(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_uint, 1)]

        self.assertEqual(X._fields_[0][1], ctypes.c_uint)
        self.assertEqual(X._fields_[0][2], 1)


