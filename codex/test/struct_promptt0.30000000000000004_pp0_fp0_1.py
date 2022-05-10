import _struct
# Test _struct.Struct

import struct
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(s.unpack(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(s.pack_into(bytearray(12), 3, 12345), None)
        self.assertEqual(bytearray(b'\x00'*12),
                         b'\x00\x00\x00\x39\x30\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(s.unpack_from(b'\x00'*12, 3), (12345,))
