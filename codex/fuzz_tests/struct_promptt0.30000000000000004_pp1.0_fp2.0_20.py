import _struct
# Test _struct.Struct.

# Test _struct.Struct.

import _struct
import unittest

class StructTestCase(unittest.TestCase):

    def test_format_error(self):
        self.assertRaises(TypeError, _struct.Struct, 'z')
        self.assertRaises(TypeError, _struct.Struct, 'P')
        self.assertRaises(TypeError, _struct.Struct, 'P', 'little')
        self.assertRaises(TypeError, _struct.Struct, 'P', 'big')
        self.assertRaises(TypeError, _struct.Struct, 'P', 'native')
        self.assertRaises(TypeError, _struct.Struct, 'P', '<')
        self.assertRaises(TypeError, _struct.Struct, 'P', '>')
        self.assertRaises(TypeError, _struct.Struct, 'P', '=')
        self.assertRaises(TypeError, _struct.Struct, 'P', '!')
        self.assertRaises(TypeError, _struct.Struct, 'P',
