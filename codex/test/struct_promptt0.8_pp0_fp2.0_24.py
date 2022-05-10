import _struct
# Test _struct.Struct
import unittest
import io
import sys

class StructTest(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.pack)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.pack(1, 2), b'\x01\x00\x00\x00')
        self.assertEqual(s.pack(*[1]), b'\x01\x00\x00\x00')
        self.assertRaises(TypeError, s.unpack, b'')
        self.assertRaises(TypeError, s.unpack, b'\x01\x00\x00')
