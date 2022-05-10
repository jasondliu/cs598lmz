import _struct
# Test _struct.Struct

import struct
import unittest
from test import support

import _struct

class StructTest(unittest.TestCase):

    def test_basics(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')

    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct, 42)
        self.assertRaises(TypeError, _struct.Struct, 'hi there')
        self.assertRaises(TypeError, _struct.Struct, 'i'*100)
