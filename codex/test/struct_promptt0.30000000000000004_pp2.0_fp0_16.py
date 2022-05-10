import _struct
# Test _struct.Struct.

import sys
import unittest

from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3)

    def test_struct_unpack(self):
        self.assertRaises(TypeError, _struct.Struct('b').unpack)
        self.assertRaises(TypeError, _struct.Struct('b').unpack, b'x', b'y')
        self.assertRaises(TypeError, _struct.Struct('b').unpack, b'x', 1, 2)
        self.assertRaises(TypeError, _struct.Struct('b').unpack, b'x', 1, 2, 3)
