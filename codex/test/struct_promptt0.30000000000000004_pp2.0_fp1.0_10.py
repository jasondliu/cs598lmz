import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct(b'')
        with self.assertRaises(TypeError):
            _struct.Struct('', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('', b'')
        with self.assertRaises(TypeError):
            _struct.Struct('', '', 42)

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
        self
