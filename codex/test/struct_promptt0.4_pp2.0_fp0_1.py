import _struct
# Test _struct.Struct

# Test the new buffer interface.

import array
from test import support
import unittest

class StructTest(unittest.TestCase):
    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct, 1)
        self.assertRaises(TypeError, _struct.Struct, 1.0)
        self.assertRaises(TypeError, _struct.Struct, ())
        self.assertRaises(TypeError, _struct.Struct, [])
        self.assertRaises(TypeError, _struct.Struct, {})
        self.assertRaises(TypeError, _struct.Struct, 'a', 'b')
        self.assertRaises(TypeError, _struct.Struct, 'a', 'b', 'c')
        self.assertRaises(TypeError, _struct.Struct, 'a', 'b', 'c', 'd')
        self.assertRaises(TypeError, _struct.Struct, 'a', 'b', 'c', 'd', 'e')
