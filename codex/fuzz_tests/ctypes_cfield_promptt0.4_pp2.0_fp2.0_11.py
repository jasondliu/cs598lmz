import ctypes
# Test ctypes.CField
#
# This test is only valid if sizeof(int) == sizeof(void*)

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.CField)]

        x = X(1, 2)
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 2)
        self.assertEqual(x[0], 1)
        self.assertEqual(x[1], 2)

        x.a = 3
        x.b = 4
        self.assertEqual(x.a, 3)
        self.assertEqual(x.b, 4)
        self.assertEqual(x[0], 3)
        self.assertEqual(x[1], 4)

        x[0] = 5
        x[1] = 6
        self.assertEqual(x.a
