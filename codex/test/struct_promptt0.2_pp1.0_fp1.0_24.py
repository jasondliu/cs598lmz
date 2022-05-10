import _struct
# Test _struct.Struct.

import unittest
import sys
import struct
import io
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
            struct.Struct('', 42)
        with self.assertRaises(struct.error):
            struct.Struct('q')
        with self.assertRaises(struct.error):
            struct.Struct('P')
        with self.assertRaises(struct.error):
            struct.Struct('cP')
        with self.assertRaises(struct.error):
            struct.Struct('Pc')
        with self.assertRaises(struct.error):
            struct.Struct('PcP')
        with self.assertRaises(struct.error):
            struct.Struct('PcPc')

