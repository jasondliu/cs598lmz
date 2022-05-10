import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import pickle
import copy

class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            struct.Struct()
        with self.assertRaises(TypeError):
            struct.Struct(42, 24)
        with self.assertRaises(TypeError):
            struct.Struct('')
        with self.assertRaises(TypeError):
            struct.Struct('abc')
        with self.assertRaises(TypeError):
            struct.Struct('abc', 42)
        with self.assertRaises(TypeError):
            struct.Struct('abc', 24)
        with self.assertRaises(TypeError):
            struct.Struct('abc', 'def')
        with self.assertRaises(TypeError):
            struct.Struct('abc', 'def', 42)
        with self.assertRaises(TypeError):
            struct.Struct('abc', 'def', 24)
        with self.assertRaises(TypeError):
            struct
