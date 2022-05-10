import _struct
# Test _struct.Struct.pack_into()

import sys
import struct
import unittest

from test import support

class StructTest(unittest.TestCase):

    def test_pack_into(self):
        # Test _struct.Struct.pack_into()
        s = _struct.Struct('i')
        buf = bytearray(s.size)
        s.pack_into(buf, 0, 1)
        self.assertEqual(buf, b'\x01\x00\x00\x00')
        s.pack_into(buf, 0, 0x01020304)
        self.assertEqual(buf, b'\x04\x03\x02\x01')
        s.pack_into(buf, 0, 0x7fffffff)
        self.assertEqual(buf, b'\xff\xff\xff\x7f')
        s.pack_into(buf, 0, -0x80000000)
        self.assertEqual(buf, b'\x00\x00\x00\x80')
        s.pack_
