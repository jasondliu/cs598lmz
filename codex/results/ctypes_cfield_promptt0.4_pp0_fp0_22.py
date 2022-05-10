import ctypes
# Test ctypes.CField.

import unittest
from test import support

from ctypes import *

class CFieldTestCase(unittest.TestCase):

    def test_field_name(self):
        class X(Structure):
            _fields_ = [("a", c_int), ("b", c_int)]

        self.assertEqual(X.a.__name__, "a")
        self.assertEqual(X.b.__name__, "b")

    def test_field_offset(self):
        class X(Structure):
            _fields_ = [("a", c_int), ("b", c_int)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, sizeof(c_int))

    def test_field_size(self):
        class X(Structure):
            _fields_ = [("a", c_int), ("b", c_int)]

        self.assertEqual(X.a.size, sizeof(c_int))
        self.assertEqual(
