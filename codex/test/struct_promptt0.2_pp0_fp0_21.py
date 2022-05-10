import _struct
# Test _struct.Struct.

import struct
import sys
import unittest

from test import support

# Test _struct.Struct.

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct.
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
        self.assertEqual(s.unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(s.unpack_from(b'\x00\x00\x00*', 3), (42,))
        self.assertEqual(s.unpack_from(bytearray(b'\x00\x00\x00*'), 3), (42,))
        self.assertEqual(s.calcsize(), 4)
        self.assertEqual(s.format, 'i')
