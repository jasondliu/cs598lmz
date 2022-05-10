import ctypes
# Test ctypes.CField
#
# This test is based on the example given in
# http://docs.python.org/library/ctypes.html#ctypes.CField

import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("upper_left", POINT),
                        ("lower_right", POINT)]

        r = RECT()
        r.upper_left.x = 10
        r.upper_left.y = 20
        r.lower_right.x = 30
        r.lower_right.y = 40

        self.assertEqual(r.upper_left.x, 10)
        self.assertEqual(r.upper_left.y, 20)
        self.assertEqual(r.lower_right.x, 30)
