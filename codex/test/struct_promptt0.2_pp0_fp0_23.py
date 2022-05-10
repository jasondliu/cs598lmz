import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 42)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 42, 42)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 42, 42, 42)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 42, 42, 42, 42)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 42, 42, 42, 42, 42, 42)
