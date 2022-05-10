import _struct
# Test _struct.Struct.pack_into() and .unpack_from()

import sys
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_pack_into(self):
        s = _struct.Struct('i')
        buf = bytearray(s.size * 2)
        s.pack_into(buf, 0, 1)
        s.pack_into(buf, s.size, 2)
        self.assertEqual(buf, b'\x01\x00\x00\x00\x02\x00\x00\x00')

    def test_unpack_from(self):
        s = _struct.Struct('i')
        buf = bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00')
        self.assertEqual(s.unpack_from(buf, 0), (1,))
        self.assertEqual(s.unpack_from(buf, s.size), (2,))

