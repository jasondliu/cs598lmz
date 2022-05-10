import _struct
# Test _struct.Struct

import unittest
import sys

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
            _struct.Struct('', '', 42)

        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.alignment, 4)

        s = _struct.Struct('P')
        self.assertEqual(s.format, 'P')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.alignment, 8)

        s = _struct.Struct
