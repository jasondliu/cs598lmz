import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 123)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 123)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 123, 456)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 123, 456,
                          789)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 123, 456,
                          789, 'abc')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 123, 456,
                          789, 'abc', 'def')
