import _struct
# Test _struct.Struct objects.

import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, b'i', b'i', b'i')
        self.assertRaises(TypeError, _struct.Struct, b'i', b'P', b'i')
        self.assertRaises(TypeError, _struct.Struct, b'P', b'P', b'i')
        self.assertRaises(TypeError, _struct.Struct, b'P', b'P', b'P')
        self.assertRaises(TypeError, _struct.Struct, b'P', b'I', b'i')
        self.assertRaises(TypeError, _struct.Struct, b'P', b'I', b'P')
        self.assertRaises(TypeError, _struct.Struct, b'P', b'I', b'I')
        self.assertRaises
