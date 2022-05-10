import ctypes
# Test ctypes.CField functionality

import unittest
from _ctypes.basics import _CData, c_int
from _ctypes import Union, Structure

class CFieldTestCase(unittest.TestCase):

    def test_simple(self):
        class X(Structure):
            _fields_ = [("a", c_int)]
        self.assertEqual(X().a, 0)
        self.assertEqual(X(a=42).a, 42)
        self.assertRaises(TypeError, X, 42)
        self.assertRaises(TypeError, X, a=3.14)
        self.assertRaises(AttributeError, getattr, X(), "b")
        X._fields_ = [("a", c_int),
                      ("b", c_int)]
        self.assertEqual(X().b, 0)
        self.assertEqual(X(42).b, 0)
        self.assertEqual(X(42, 43).b, 43)
        self.assertRaises(TypeError, X, 42, 43, 44)

   
