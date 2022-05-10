import ctypes
# Test ctypes.CField.
# The CField class is a subclass of _CData that adds the field offset
# and bitshift information.

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.c.offset, 8)

    def test_union(self):
        class X(ctypes.Union):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 0)
        self
