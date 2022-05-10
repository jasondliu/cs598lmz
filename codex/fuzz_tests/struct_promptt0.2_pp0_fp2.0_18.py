import _struct
# Test _struct.Struct.

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(42), '*\x00\x00\x00')
        self.assertEqual(s.unpack('*\x00\x00\x00'), (42,))
        self.assertRaises(TypeError, s.pack, 42, 42)
        self.assertRaises(TypeError, s.unpack, '*\x00\x00\x00', 42)
        self.assertRaises(TypeError, s.unpack, '*\x00\x00')
        self.assertRaises(TypeError, s.unpack, '*\x00\x00\x00\x00')
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.unpack)
        self.
