import _struct
# Test _struct.Struct

import unittest
from test import support

# Test the basic functionality

class StructTestCase(unittest.TestCase):
    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i')
        self.assertRaises(TypeError, _struct.Struct, 'i', 'ii')
        self.assertRaises(TypeError, _struct.Struct, 'i', 'iii')
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i'*129)
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i'*256)
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i'*257)
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i'*65536)
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i'*65537)
        self.assertRaises(TypeError, _struct.Struct, 'i', '
