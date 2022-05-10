import ctypes
# Test ctypes.CField

# Includes
import unittest
from ctypes import *

class CFieldTestCase(unittest.TestCase):

    def test_c_field(self):
        class Record(Structure):
            _fields_ = [("x", c_int),
                        ("y", c_int)]

        r = Record()
        self.assertRaises(AttributeError, getattr, r, "__dict__")
        self.assertRaises(AttributeError, getattr, r, "x")
        self.assertRaises(AttributeError, getattr, r, "y")
        self.assertTrue(r.x == r.y == 0)
        r = Record(1, 2)
        self.assertTrue(r.x == 1)
        self.assertTrue(r.y == 2)

        # Read-only attribute
        self.assertRaises(AttributeError, setattr, r, "x", 2)
        self.assertRaises(AttributeError, setattr, r, "y", 2)

        # Non-existing attribute
        self.assertRaises(AttributeError
