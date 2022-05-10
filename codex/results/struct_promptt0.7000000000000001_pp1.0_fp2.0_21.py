import _struct
# Test _struct.Struct.

import struct
import unittest

from test import support

# These tests are too trivial to be worth writing in C.

class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
        self.assertEqual(s.unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(s.pack_into(bytearray(b'\0' * 8), 4, 42), None)
        self.assertEqual(bytearray(b'\0'*4 + b'*\x00\x00\x00'),
                         s.pack_into(bytearray(b'\0' * 8), 4, 42))
        self.assertEqual(s.unpack_from(b'\0\0\0\0*\x00
