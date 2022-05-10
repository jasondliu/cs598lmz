import ctypes
# Test ctypes.CField
#

import unittest
from ctypes import *

class t_cfield(unittest.TestCase):
    def test_cfield(self):
        class X(Structure):
            _fields_ = [("a", c_int), ("b", c_int)]

        self.assertEqual(sizeof(X), 8)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)

        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.b.size, 4)

        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.b.index, 1)

        self.assertEqual(X.a.pack, 1)
        self.assertEqual(X.b.pack, 1)

        self.assertEqual(X.a.bitsize, 32)
        self.assertEqual(X.b.bitsize, 32)

        self.assertEqual(X.a
