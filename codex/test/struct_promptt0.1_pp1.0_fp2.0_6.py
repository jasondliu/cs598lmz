import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6)
