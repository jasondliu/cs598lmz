import _struct
# Test _struct.Struct

import unittest
from test import support
from _testcapi import getargs_g

class StructTestCase(unittest.TestCase):

    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '@')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '@', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', '@')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', '@', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '@', '=')
