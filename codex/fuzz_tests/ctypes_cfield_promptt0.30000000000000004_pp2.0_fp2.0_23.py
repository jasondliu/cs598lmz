import ctypes
# Test ctypes.CField
#
# This test is a bit different from the others, because it doesn't
# test the ctypes module itself, but the CField class.  It is
# included in the ctypes test suite because it's the only place where
# it can be tested.

import unittest
from ctypes import *

class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class X(Structure):
            _fields_ = [("a", c_int),
                        ("b", c_int)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, sizeof(c_int))

        self.assertEqual(X.a.size, sizeof(c_int))
        self.assertEqual(X.b.size, sizeof(c_int))

        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.b.index, 1)

        self.assertEqual(X.a.pack, 1)
        self.assert
