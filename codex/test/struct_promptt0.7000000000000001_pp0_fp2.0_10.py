import _struct
# Test _struct.Struct

# This is not a very thorough test, but you can add more if you wish.

import _struct
import unittest
import sys
import struct

class StructTest(unittest.TestCase):

    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct, 'a')
        self.assertRaises(TypeError, _struct.Struct, 2)

    def test_size(self):
        self.assertRaises(TypeError, _struct.Struct('@').size)
        self.assertRaises(TypeError, _struct.Struct('@').size, None)
        self.assertEqual(_struct.Struct('b').size, 1)
        self.assertEqual(_struct.Struct('h').size, 2)
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('l').size, 4)
        self.assertEqual(_struct.Struct('q').size, 8)
        self.assertEqual(_struct.Struct('n').size, 2)
       
