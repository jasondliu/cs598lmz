import _struct
# Test _struct.Struct
import struct
import sys
import unittest

class StructTest(unittest.TestCase):

    def test_basics(self):
        s = _struct.Struct('hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))
        self.assertEqual(s.unpack_from(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))
        self.assertEqual(s.unpack_from(b'x' * 8 + b'\x01\x00\x02\x00\x00\x00\x00\x03', 8), (1, 2
