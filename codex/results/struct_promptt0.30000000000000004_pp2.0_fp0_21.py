import _struct
# Test _struct.Struct

import unittest
from test import support

# A few tests to check that the _struct.Struct class works as expected.

class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('abc')
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 0)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', -1)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 1<<32)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 1<<64)
       
