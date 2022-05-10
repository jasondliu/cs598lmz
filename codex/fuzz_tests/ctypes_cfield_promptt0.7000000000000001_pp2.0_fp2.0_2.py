import ctypes
# Test ctypes.CField

# from ctypes import *
import unittest
from ctypes.test.test_structures import getargs

class CFieldTestCase(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

        self.assertEqual(str(X.a), "a")
        self.assertEqual(str(X.b), "b")

        self.assertRaises(IndexError, X._fields_.__getitem__, -1)
        self.assertRaises(IndexError, X._fields_.__getitem__, 2)

    def test_offsets(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b",
