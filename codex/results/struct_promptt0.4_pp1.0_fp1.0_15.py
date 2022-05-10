import _struct
# Test _struct.Struct.iter_unpack()
import _testcapi
import array
import itertools
import os
import sys
import unittest
from test import support

def get_size(fmt):
    return struct.calcsize(fmt)

class StructTest(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct, 'abcdefg')
        self.assertRaises(TypeError, _struct.Struct, 'abcdefg', 0)
        self.assertRaises(TypeError, _struct.Struct, 'abcdefg', '0')
        self.assertRaises(TypeError, _struct.Struct, 'abcdefg', '0', 0)
        self.assertRaises(TypeError, _struct.Struct, 'abcdefg', '0', '0')
        self.assertRaises(TypeError, _struct.Struct, 'abcdefg', '0', '0', 0)
        self.assertRaises(TypeError, _struct.Struct, 'abcdefg', '0',
