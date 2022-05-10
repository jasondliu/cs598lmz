import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6, 'def')
        self.assertRaises
