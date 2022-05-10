import ctypes
# Test ctypes.CField.

import unittest
from test import test_support

import _ctypes_test

class CFieldTestCase(unittest.TestCase):
    def test_setattr(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        x = X()
        x.a = 42
        self.assertEqual(x.a, 42)

        self.assertRaises(TypeError, setattr, x, "a", "hello")
        self.assertRaises(TypeError, setattr, x, "b", "hello")

    def test_getattr(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        x = X()
        self.assertEqual(x.a, 0)

        self.assertRaises(AttributeError, getattr, x, "b")

    def test_c_int(self):
        class X(ctypes.Structure):
            _fields_ = [("a", c
