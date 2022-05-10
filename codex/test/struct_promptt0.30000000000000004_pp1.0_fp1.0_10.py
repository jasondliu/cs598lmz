import _struct
# Test _struct.Struct

# This test is not complete, but it's better than nothing.

import _struct
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertRaises(TypeError, s.pack, 'a')
        self.assertRaises(TypeError, s.unpack, 1)
        self.assertRaises(TypeError, s.unpack, b'\x01\x00\x00')
        self.assertRaises(TypeError, s.unpack, b'\x01\x00\x00\x00\x00')

    def test_struct_format(self):
        self.assertRaises
