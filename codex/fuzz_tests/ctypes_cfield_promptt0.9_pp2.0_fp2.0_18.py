import ctypes
# Test ctypes.CField
from ctypes.test.test_cfield import Point, SmallPoint, TStructure, TUnion, X, Y, ZW
from ctypes import *
from ctypes.test import is_resource_enabled
import unittest
from test import support

class Structures(unittest.TestCase):
    def setUp(self):
        # every test needs to create and initialize a struct/union instance
        self.v = TStructure()

    def test_fields(self):
        self.assertEqual(self.v._fields_, [("a", c_int32), ("b", c_int32), ("c", c_int32)])

    def test_repr(self):
        self.assertEqual(repr(self.v), "<c_test_cfield.TStructure object at 0x%x>" %
                                     (id(self.v),))

    def test_setattr_invalid(self):
        # all three fields are read-only
        self.assertRaises(AttributeError, setattr, self.v, "a", 11)

