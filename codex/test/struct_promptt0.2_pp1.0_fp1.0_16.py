import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import array

from test import support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        # Test _struct.Struct objects
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.unpack(b'abcd'), (1684234849,))
        self.assertEqual(s.pack(1684234849), b'abcd')
        self.assertEqual(s.pack_into(bytearray(4), 0, 1684234849), 4)
        self.assertEqual(s.unpack_from(b'efghi', 1), (1690906049,))
        self.assertEqual(s.unpack_from(memoryview(b'efghi'), 1), (1690906049,))
