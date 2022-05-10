import ctypes
# Test ctypes.CField.

from ctypes import *

# Types defined in C
class Structure(Structure):
    _fields_ = [("x", c_int)]

class Union(Union):
    _fields_ = [("x", c_int)]

class Enum(Enumeration):
    x = 1

class CFieldTestCase(unittest.TestCase):
    def test_field_name(self):
        self.assertEqual(ctypes.Field(Structure, "x").name, "x")
        self.assertEqual(ctypes.Field(Structure, "y", c_int).name, "y")
        self.assertRaises(ValueError, ctypes.Field, Structure, "y")

    def test_field_type(self):
        self.assertEqual(ctypes.Field(Structure, "x").type, c_int)
        self.assertEqual(ctypes.Field(Structure, "y", c_short).type, c_short)
        self.assertRaises(ValueError, ctypes.Field, Structure, "y
