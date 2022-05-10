import _struct
# Test _struct.Struct.

import sys
import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('', b'')
        with self.assertRaises(TypeError):
            _struct.Struct('', bytearray())
        with self.assertRaises(TypeError):
            _struct.Struct('', memoryview(b''))
        with self.assertRaises(TypeError):
            _struct.Struct('', bytearray(b''))

        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(
