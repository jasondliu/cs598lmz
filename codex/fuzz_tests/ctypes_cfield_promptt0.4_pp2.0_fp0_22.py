import ctypes
# Test ctypes.CField

# This test is for the CField class.
# CField is used to represent a field in a C structure.
# We use it in the Structure class to create a structure class.

import unittest
from test import support

class CFoo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class CFieldTestCase(unittest.TestCase):
    def test_field_name(self):
        self.assertEqual(CFoo._fields_[0].name, "a")

    def test_field_type(self):
        self.assertEqual(CFoo._fields_[0].ctype, ctypes.c_int)

    def test_field_offset(self):
        self.assertEqual(CFoo._fields_[0].offset, 0)

    def test_field_size(self):
        self.assertEqual(CFoo._fields_[0].size, ctypes.sizeof(ctypes.c_int))

    def test_field_bits(self):
        self.assertE
