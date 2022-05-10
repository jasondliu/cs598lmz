import _struct
# Test _struct.Struct.
# This tests the methods of the Struct class, not the module.
import unittest
import sys
import io

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
            _struct.Struct('', '@')
        with self.assertRaises(TypeError):
            _struct.Struct('', '@', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('', '@', 0, 42)

        s = _struct.Struct('abc')
        self.assertEqual(s.size, 3)
        self.assertEqual(s.format, 'abc')
