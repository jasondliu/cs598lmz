import _struct
# Test _struct.Struct.

import unittest
import sys
import struct
import io
import pickle
import copy
import test.support

class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            struct.Struct()
        with self.assertRaises(TypeError):
            struct.Struct(42, 42)
        with self.assertRaises(TypeError):
            struct.Struct('')
        with self.assertRaises(TypeError):
            struct.Struct('abc\0\0')
        with self.assertRaises(TypeError):
            struct.Struct('abc\0\0', 42)
        with self.assertRaises(TypeError):
            struct.Struct('abc\0\0', 'abc\0\0')
        with self.assertRaises(TypeError):
            struct.Struct('abc\0\0', 'abc\0\0', 42)
        with self.assertRaises(TypeError):
            struct.Struct('abc\0\0', 'abc\0\0', '
