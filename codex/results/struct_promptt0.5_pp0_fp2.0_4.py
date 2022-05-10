import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTest(unittest.TestCase):

    def test_Struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('x')
        with self.assertRaises(TypeError):
            _struct.Struct('x', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('x', 'x')
        with self.assertRaises(TypeError):
            _struct.Struct('x', '@')
        with self.assertRaises(TypeError):
            _struct.Struct('x', '@', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('x', '@', 'x')
        with self.assertRaises(TypeError):
            _
