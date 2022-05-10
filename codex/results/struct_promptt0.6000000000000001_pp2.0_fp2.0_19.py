import _struct
# Test _struct.Struct
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_Struct(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6, 7,
                          8)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6, 7,
                          8, 9, 10)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6, 7,
                          8, 9, 10, 11, 12)
