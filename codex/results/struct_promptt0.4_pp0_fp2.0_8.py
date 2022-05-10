import _struct
# Test _struct.Struct.

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi',
                          'jkl')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi',
                          'jkl', 'mno')

    def test_size(self):
        self.assertEqual(_struct.Struct('x').size, 1)
        self.assertEqual(_struct.Struct('c').size, 1)
        self.assertEqual(_struct.Struct('b
