import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import support

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(1), struct.pack('i', 1))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00junk'), (1,))
        self.assertEqual(s.unpack_from(memoryview(b'\x01\x00\x00\x00junk')), (1,))
        self.assertEqual(s.unpack_from(bytearray(b'\x01\x00\x00\x00junk')), (1,))
        self.
