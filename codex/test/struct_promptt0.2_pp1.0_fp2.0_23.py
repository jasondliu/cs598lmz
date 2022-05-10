import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import pickle
import copy
import test.support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(b'abc')
        with self.assertRaises(TypeError):
            _struct.Struct(b'abc', b'def')
        with self.assertRaises(TypeError):
            _struct.Struct(b'abc', b'def', b'ghi')
        with self.assertRaises(TypeError):
            _struct.Struct(b'abc', b'def', b'ghi', b'jkl')
        with self.assertRaises(TypeError):
            _struct.Struct(b'abc', b'def', b'ghi', b'jkl', b'mno')
