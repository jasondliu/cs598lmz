import ctypes
# Test ctypes.CField and ctypes.CFieldSet
#
# The CFieldSet class makes it easy to get at individual bits
# and full bytes of a ctypes data type.  It's used internally
# in the creation of ctypes structures, and can be used directly.
#
# This file tests the CFieldSet class, and the CField class
# used to construct a CFieldSet.

import unittest

class CFieldSetTestCase(unittest.TestCase):
    def _test_CFS_init(self, cfs):
        self.assertTrue(0 <= cfs.offset and cfs.offset < 8)
        self.assertTrue(0 < cfs.size and cfs.size < 9)
        self.assertEqual(cfs.size + cfs.offset, 8)

        self.assertEqual(cfs.mask,
                         sum([1 << (8-bit-1) for bit in range(cfs.offset, 8)]))
        self.assertEqual(cfs.mask, 0xff >> cfs.offset)
        self.assertEqual(cfs.
