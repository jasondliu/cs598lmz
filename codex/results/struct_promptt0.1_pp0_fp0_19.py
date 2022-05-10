import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno', 'p
