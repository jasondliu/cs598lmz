import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('i', '')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'abc')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'abc', '')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'abc', 'def')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'abc', 'def', '')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'abc', 'def', 'ghi')
        with self.assertRaises(TypeError):
            _struct.Struct('
