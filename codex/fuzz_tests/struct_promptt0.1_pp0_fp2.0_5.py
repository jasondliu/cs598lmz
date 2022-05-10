import _struct
# Test _struct.Struct

import unittest
import sys
import struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            struct.Struct()
        with self.assertRaises(TypeError):
            struct.Struct(42)
        with self.assertRaises(TypeError):
            struct.Struct('')
        with self.assertRaises(TypeError):
            struct.Struct('', 42)
        with self.assertRaises(TypeError):
            struct.Struct('', '')
        with self.assertRaises(TypeError):
            struct.Struct('', '', 42)
        with self.assertRaises(TypeError):
            struct.Struct('', '', '')
        with self.assertRaises(TypeError):
            struct.Struct('', '', '', 42)
        with self.assertRaises(TypeError):
            struct.Struct('', '', '', '')
        with self.assertRaises(TypeError):
            struct.Struct('', '', '', '', 42
