import _struct
# Test _struct.Struct

import unittest
import sys
import struct

# test data

s = b'\x12\x34\x56\x78'

# test code

class StructTest(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(0x12345678), b'\x12\x34\x56\x78')
        self.assertEqual(s.unpack(b'\x12\x34\x56\x78'), (0x12345678,))
        self.assertEqual(s.unpack_from(b'\x00\x00\x00\x00\x12\x34\x56\x78'),
                         (0x12345678,))
