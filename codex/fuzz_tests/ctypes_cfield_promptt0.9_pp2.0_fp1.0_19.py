import ctypes
# Test ctypes.CField and ctypes.CFUNCTYPE

import sys, unittest
from ctypes import *
from test.test_support import run_unittest

class FieldTestCase(unittest.TestCase):
    def test_bitfield(self):
        if sys.byteorder == "big":
            FF = c_ubyte
            BFA, BFB, BFC, BFD = 7, 8, 12, 7
        else:
            FF = c_uint
            BFA, BFB, BFC, BFD = 16, 24, 0, 16

        class X(BigEndianStructure):
            _fields_ = [
                ("a", FF, BFA),
                ("b", FF, BFB),
                ("c", FF, BFC),
                ("d", FF, BFD),
            ]

        self.assertEqual(sizeof(X), sizeof(FF))

        ff = X(0).a
        self.assertEqual((ff.__index__(), ff._length_), (BFA, BFB))
        ff = X(0).b

