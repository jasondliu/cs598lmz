import ctypes
# Test ctypes.CField
import _ctypes
import unittest

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class FieldTestCase(unittest.TestCase):
    def test_field(self):
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.a.index, 0)

    def test_field_in_union(self):
        class Y(ctypes.Union):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(Y.a.offset, 0)
        self.assertEqual(Y.a.size, 4)
        self.assertEqual(Y.a.index, 0)

    def test_anonymous_field(self):
        class Y(ctypes.Union):
            _fields_ = [("", ctypes.c_int)]
        self.assertEqual(Y.a.offset, 0)
        self.assert
