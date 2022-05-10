import _struct
# Test _struct.Struct.pack_into()

import sys
import struct
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_pack_into(self):
        # Issue #1202: pack_into() should accept buffer objects
        s = struct.Struct('i')
        buf = bytearray(s.size)
        s.pack_into(buf, 0, 12345)
        self.assertEqual(s.unpack(buf), (12345,))

        buf = memoryview(buf)
        s.pack_into(buf, 0, 67890)
        self.assertEqual(s.unpack(buf), (67890,))

    def test_pack_into_buffer(self):
        # Issue #1202: pack_into() should accept buffer objects
        s = struct.Struct('i')
        buf = bytearray(s.size)
        s.pack_into(buf, 0, 12345)
        self.assertEqual(s.unpack(buf), (12345,))

        buf =
