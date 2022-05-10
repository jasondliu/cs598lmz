import _struct
# Test _struct.Struct
import sys
import unittest
from test import support

# Basic struct string test

class StructTest(unittest.TestCase):

    def test_basic(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.pack_into(b'####', 0, 1), None)
        self.assertEqual(b'####', b'\x01\x00\x00\x00')

    def test_buffer(self):
        s = _struct.Struct('i')
        b = bytearray(4)
        self.assertEqual(s.pack_
