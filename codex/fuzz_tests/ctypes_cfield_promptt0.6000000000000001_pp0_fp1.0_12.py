import ctypes
# Test ctypes.CField.

import unittest

from ctypes import *

class CFieldTest(unittest.TestCase):
    def test_basic(self):
        class POINT(Structure):
            _fields_ = [("x", c_int),
                        ("y", c_int)]

        p = POINT()
        p.x = 1
        p.y = 2
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_subclass(self):
        class POINT(Structure):
            _fields_ = [("x", c_int),
                        ("y", c_int)]

        class POINTF(POINT):
            _fields_ = [("z", c_float)]

        p = POINTF()
        p.x = 1
        p.y = 2
        p.z = 3.0
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 3
