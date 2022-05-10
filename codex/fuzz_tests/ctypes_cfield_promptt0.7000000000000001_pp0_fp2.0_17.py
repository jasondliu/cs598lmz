import ctypes
# Test ctypes.CField
#
# The CField object is used by the CType object.  It represents a
# field of the CType.  The only access is through the __getitem__
# method.

import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):

    def test_bitfield(self):
        # Check whether bitfields work properly
        #
        # The layout of the following structure is (on a little-endian
        # machine):
        #
        # struct S {
        #     unsigned int a : 4;
        #     unsigned int b : 8;
        #     unsigned int c : 20;
        # };
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_uint, 4),
                        ("b", ctypes.c_uint, 8),
                        ("c", ctypes.c_uint, 20)]

        s = S()
        s.a = 0x1
        s.b = 0x23
        s.c = 0x456
        self.assertEqual
