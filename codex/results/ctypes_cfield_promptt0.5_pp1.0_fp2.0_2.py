import ctypes
# Test ctypes.CField
#
# Note: This is a private class, not normally accessible from Python.
#
# It is used to implement the _fields_ attribute of structured ctypes.

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(S._fields_[0].__class__, ctypes.CField)
        self.assertEqual(S._fields_[0].name, "x")
        self.assertEqual(S._fields_[0].ctype, ctypes.c_int)

    def test_array(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int * 2)]
        self.assertEqual(S._fields_[0].__class__, ctypes.CField)
        self.assertEqual(S._fields_[0].name, "x")
       
