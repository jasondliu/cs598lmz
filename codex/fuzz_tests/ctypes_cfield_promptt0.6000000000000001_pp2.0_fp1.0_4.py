import ctypes
# Test ctypes.CField.

import unittest
from test import support
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int), ("b", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class CFieldTestCase(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(X.a, Y.a)
        self.assertEqual(X.a, Z.a)
        self.assertEqual(X.b, Y.b)
        self.assertEqual(X.b, Z.b)

    def test_inequality(self):
        self.assertNotEqual(X.a, X.b)
        self.assertNotEqual(Y.a, Y.b)
        self.assertNotEqual(Z.a, Z.
