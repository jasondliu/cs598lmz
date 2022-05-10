import _struct
# Test _struct.Struct

import sys
import unittest


class StructTest(unittest.TestCase):

    def test_format(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(None)
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct(b'')
        with self.assertRaises(TypeError):
            _struct.Struct('>')
        self.assertEqual(_struct.Struct('x').format, b'x')
        self.assertEqual(_struct.Struct('xi').format, b'xi')
        self.assertEqual(_struct.Struct('x').format, b'x')
        self.assertEqual(_struct.Struct('xi').format, b'xi')
        self.assertEqual(_struct.Struct('!').format, b'!')
        self.assertEqual(_struct.Struct('!i').format, b'!i
