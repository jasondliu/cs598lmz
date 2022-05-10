import ctypes
# Test ctypes.CField.get_field_type()
# Check that for fields of a primitive type, get_field_type() returns
# that type.

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_primitive_types(self):
        CField = ctypes.CField
        self.assertIs(CField(ctypes.c_int, 'x').get_field_type(), ctypes.c_int)
        self.assertRaises(AttributeError, CField, ctypes._CFuncPtr, 'x')

    def test_struct_types(self):
        # ctypes.POINTER(ctypes.Structure) was broken
        class POINTER(ctypes.Structure):
            _fields_ = [('p', ctypes.POINTER(ctypes.c_int))]

        ptr = POINTER()
        self.assertRaises(AttributeError, ctypes.CField, ptr, 'p')

    def test_SizedCDataType(self):
        # Issue2854
        class SizedCDataType(
