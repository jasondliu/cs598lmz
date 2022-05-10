import ctypes
# Test ctypes.CField
#
# This tests the CField object, which is used by the CStructure object.
#
# The CField object is used to keep track of the offsets and types of
# the fields in a CStructure.

import unittest
from test import test_support

import ctypes

class CFieldTestCase(unittest.TestCase):
    def test_field(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_double)]

        self.assertEqual(X._fields_[0].offset, 0)
        self.assertEqual(X._fields_[1].offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int) + ctypes.sizeof(ctypes.c_double))

    def test_pack(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes
