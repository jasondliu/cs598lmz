import _struct
# Test _struct.Struct()

# XXX This should be part of test_struct

import _struct
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertRaises(TypeError, s.pack, 'abc')
        self.assertRaises(TypeError, s.unpack, b'abc')
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.unpack, b'\x01\x00\x00\x00', 4)
        self.assertRaises(TypeError, s.pack)
