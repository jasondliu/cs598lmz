import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_field_type(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(type(X.a), ctypes.CField)

    def test_field_type_name(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.__name__, "a")

    def test_field_type_doc(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.__doc__, "c_int(a)")

    def test_field_type_get(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        x =
