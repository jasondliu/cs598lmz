import _struct
# Test _struct.Struct.

import unittest
from test import support

import struct

class StructTestCase(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc%')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 123)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 123, 456)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 123, 456, 789)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 123, 456, 789,
                          'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 123, 456, 789,
                          'def', 'ghi')
