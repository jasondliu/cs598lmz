import ctypes
# Test ctypes.CField, ctypes.Field

import unittest
from test import support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class FieldTestCase(unittest.TestCase):
    def test_field_offset(self):
        self.assertEqual(ctypes.c_int.in_dll(X, "a").value, 0)
        self.assertEqual(ctypes.c_int.in_dll(X, "b").value, 4)
        self
