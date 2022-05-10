import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('abc%')
        with self.assertRaises(TypeError):
            _struct.Struct('abc%d')
        with self.assertRaises(TypeError):
            _struct.Struct('abc%%d')
        with self.assertRaises(TypeError):
            _struct.Struct('abc%(foo)d')
        with self.assertRaises(TypeError):
            _struct.Struct('abc%(foo')

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
