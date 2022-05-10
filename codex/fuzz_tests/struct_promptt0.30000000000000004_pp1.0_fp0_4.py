import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x00\x01\x00\x00'), (65536,))
        self.assertEqual(s.unpack(b'\x00\x00\x01\x00'), (1<<16,))
        self.assertEqual(s.unpack(b'\x00\x00\x00\x01'), (1<<24,))
        self.assertRaises(TypeError, s.unpack, 'abc')
        self.assertRaises(TypeError, s.unpack, 1)
        self.assertRaises(TypeError, s.unpack, 1.0)
        self.assertRaises(TypeError, s.unpack, [1])

