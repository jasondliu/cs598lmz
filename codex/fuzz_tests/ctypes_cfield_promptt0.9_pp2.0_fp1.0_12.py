import ctypes
# Test ctypes.CField primitive type

import unittest, sys
from test import support

class StructFieldTest(unittest.TestCase):

    def test_field_name(self):
        class X(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int)]
        self.assertEqual(X._fields_[0][0], "foo")

    def test_field_type(self):
        class X(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1], ctypes.c_int)

    def test_field_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int)]
        self.assertEqual(X.foo.offset, ctypes.c_int.offset)

    def test_fields(self):
        class X(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int), ("bar", ctypes.
