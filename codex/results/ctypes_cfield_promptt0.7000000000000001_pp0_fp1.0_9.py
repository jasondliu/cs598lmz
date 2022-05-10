import ctypes
# Test ctypes.CField.
import unittest
from test import support
import sys
import _ctypes_test

class CFieldTestCase(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [
                ('a', ctypes.c_int),
                ('b', ctypes.c_char)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int) + ctypes.sizeof(ctypes.c_char))

    def test_array(self):
        class X(ctypes.Structure):
            _fields_ = [
                ('a', ctypes.c_int * 3),
                ('b', ctypes.c_char * 4)]
        self.assertEqual(ctypes.sizeof(X), 12 + 4)
        self.assertEqual(ctypes.sizeof(X.a), 12)
        self.assertEqual(ctypes.sizeof(X.b), 4)

    def test_nested_struct(self
