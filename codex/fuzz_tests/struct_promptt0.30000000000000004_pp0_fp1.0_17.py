import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, '', 'Z')
        self.assertRaises(TypeError, _struct.Struct, '', 'Z', 'Z')
        self.assertRaises(TypeError, _struct.Struct, '', '=')
        self.assertRaises(TypeError, _struct.Struct, '', '=', '=')
        self.assertRaises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z')
        self.assertRaises(TypeError, _struct.Struct, '', 'Z', 'Z', 'Z', 'Z')
        self.assertRaises(TypeError, _struct.Struct, '', '=', '=', '=')
        self.assertRaises(TypeError, _struct.Struct, '', '=', '=', '=',
