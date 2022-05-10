import _struct
# Test _struct.Struct.unpack_from() method.

import struct
import sys
import unittest

from test.support import bigmemtest

class StructTest(unittest.TestCase):

    def test_unpack_from(self):
        # Test _struct.Struct.unpack_from() method.

        S = _struct.Struct("i")
        DATA = b"abcd01234567"

        # Test wrong arguments.
        self.assertRaises(TypeError, S.unpack_from)
        self.assertRaises(TypeError, S.unpack_from, DATA)
        self.assertRaises(TypeError, S.unpack_from, DATA, 1, 2, 3, 4)

        self.assertEqual(S.unpack_from(DATA, 1), (0x34333231,))
        self.assertEqual(S.unpack_from(DATA, 1, 2), (0x34333231,))
        self.assertEqual(S.unpack_from(memoryview(DATA), 1), (0x34333231,))
       
