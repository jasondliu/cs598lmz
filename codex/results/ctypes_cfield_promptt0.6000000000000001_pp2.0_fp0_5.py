import ctypes
# Test ctypes.CField.

import unittest
from ctypes import *
from test import support

class CFieldTestCase(unittest.TestCase):

    def test_bitfields(self):
        class X(Structure):
            _fields_ = [("a", c_byte, 2),
                        ("b", c_byte, 3),
                        ("c", c_byte, 3)]

        x = X()

        x.a = 1
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 0)
        self.assertEqual(x.c, 0)

        x.b = 4
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 4)
        self.assertEqual(x.c, 0)

        x.c = 5
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 4)
        self.assertEqual(x.c, 5)

        x.a = 3
        self.assertEqual
