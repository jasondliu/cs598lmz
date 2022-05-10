import _struct
# Test _struct.Struct objects
import unittest
import sys
import io
import _testcapi

class StructTest(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6, 7)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3, 4, 5, 6, 7, 8)
