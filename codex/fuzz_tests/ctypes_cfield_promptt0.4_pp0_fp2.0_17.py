import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X().a, 0)

    def test_simple_2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int), ("b", ctypes.c_int)])
        self.assertEqual(X().a, 0)
        self.assertEqual(X().b, 0)

    def test_simple_3(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int), ("b
