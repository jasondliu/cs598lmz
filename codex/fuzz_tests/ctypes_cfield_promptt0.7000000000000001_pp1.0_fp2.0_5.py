import ctypes
# Test ctypes.CField

import unittest
from test import test_support

from ctypes import *

class CFieldTestCase(unittest.TestCase):
    def test_field_basic(self):
        class X(Structure):
            _fields_ = [("one", c_int)]
        self.assertEqual(X.one.offset, 0)
        self.assertEqual(X.one.size, sizeof(c_int))
        self.assertEqual(X.one.index, 0)
        self.assertEqual(X.one.pack, 1)
        self.failUnless(isinstance(X.one, CField))

    def test_field_array(self):
        class X(Structure):
            _fields_ = [("one", c_int * 3)]
        self.assertEqual(X.one.offset, 0)
        self.assertEqual(X.one.size, sizeof(c_int) * 3)
        self.assertEqual(X.one.index, 0)
        self.assertEqual(X.one.pack
