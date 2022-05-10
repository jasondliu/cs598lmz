import _struct
# Test _struct.Struct, _struct.pack, _struct.unpack

import sys
import unittest

from test import support

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct object
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')
        self.assertRaises(TypeError, s)
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.unpack)
        self.assertRaises(TypeError, s.iter_unpack)

    def test_pack(self):
        # Test _struct.pack
        self.assertEqual(_struct.pack('i', 0), b'\0\0\0\0')
        self.assertEqual(_struct.pack('i', 1), b'\0\0\0\1')
