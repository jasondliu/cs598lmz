import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, "")
        self.assertRaises(TypeError, _struct.Struct, "", "")
        self.assertRaises(TypeError, _struct.Struct, "", "", "")
        self.assertRaises(TypeError, _struct.Struct, "", "", "", "")
        self.assertRaises(TypeError, _struct.Struct, "", "", "", "", "")
        self.assertRaises(TypeError, _struct.Struct, "", "", "", "", "", "")

    def test_struct_format(self):
        self.assertRaises(TypeError, _struct.Struct, "")
        self.assertRaises(TypeError, _struct.Struct, "", "")
