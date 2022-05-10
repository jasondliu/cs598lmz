import _struct
# Test _struct.Struct.

import unittest
import sys
import struct
import io

class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            struct.Struct()
        with self.assertRaises(TypeError):
            struct.Struct(42, 24)
        with self.assertRaises(TypeError):
            struct.Struct('')
        with self.assertRaises(TypeError):
            struct.Struct('', 42)
        with self.assertRaises(TypeError):
            struct.Struct('', '')
        with self.assertRaises(struct.error):
            struct.Struct('q')
        with self.assertRaises(struct.error):
            struct.Struct('P')
        with self.assertRaises(struct.error):
            struct.Struct('P', 'little')
        with self.assertRaises(struct.error):
            struct.Struct('P', 'big')
        with self.assertRaises(struct.error):
            struct.Struct('P', 'native')
       
