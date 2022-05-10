import _struct
# Test _struct.Struct

import struct
import sys
import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(1)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 1)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 'def')
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 'def', 1)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 'def', 'ghi')
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 'def', 'ghi', 1)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 'def', 'ghi', 'jkl')
