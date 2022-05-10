import _struct
# Test _struct.Struct.pack_into()

import sys
import unittest
from test import support

class PackIntoTest(unittest.TestCase):

    def test_pack_into(self):
        # Test _struct.Struct.pack_into()
        s = _struct.Struct('i')
        buf = bytearray(s.size * 2)
        s.pack_into(buf, 0, 1)
        s.pack_into(buf, s.size, 2)
        self.assertEqual(buf, b'\x01\x00\x00\x00\x02\x00\x00\x00')

    def test_pack_into_buffer(self):
        # Test _struct.Struct.pack_into() with a buffer object
        s = _struct.Struct('i')
        buf = buffer(bytearray(s.size * 2))
        s.pack_into(buf, 0, 1)
        s.pack_into(buf, s.size, 2)
