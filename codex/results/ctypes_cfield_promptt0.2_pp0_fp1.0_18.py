import ctypes
# Test ctypes.CField

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):

    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

    def test_bitfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1),
                        ("b", ctypes.c_int, 2),
                        ("c", ctypes.c_int, 3),
                        ("d", ctypes.c_int, 4),
                        ("e", ctypes.c_int, 5),
                        ("f", ctypes.c_int, 6),
                        ("g", ctypes.c_int, 7),
                        ("h", ctypes.c_int, 8),
