import ctypes
# Test ctypes.CField

import unittest
from test import support

class CFieldTest(unittest.TestCase):

    def test_simple(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT()
        pt.x = 1
        pt.y = 2
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)
        self.assertEqual(pt[0], 1)
        self.assertEqual(pt[1], 2)
        self.assertEqual(pt[:], (1, 2))

    def test_subclass(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]
        rect
