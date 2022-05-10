import _struct
# Test _struct.Struct.pack_into() on arrays.
import array
import sys
import unittest
from test.support import little_endian, big_endian, run_unittest, swap_attr

class StructArrayTest(unittest.TestCase):

    def test_pack_into(self):
        # Test packing into an array from a sequence.
        a = array.array("b", range(10))
        Struct("HHH").pack_into(a, 0, 1, 2, 3)
        self.assertEqual(list(a), [1, 0, 2, 0, 3, 0, 6, 7, 8, 9])

    def test_pack_into_overflow(self):
        # Test packing into an array from a sequence.
        a = array.array("i", range(10))
        an = array.array("i", range(10))
        try:
            Struct("bi").pack_into(a, 0, 1, 2)
        except OverflowError:
            pass
        else:
            self.assertTrue(False)
