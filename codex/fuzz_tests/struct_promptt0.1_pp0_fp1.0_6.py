import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io

from test import support

class StructTestCase(unittest.TestCase):

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
        with self.assertRaises(struct.error):
            struct.Struct('x')
        with self.assertRaises(struct.error):
            struct.Struct('@')
        with self.assertRaises(struct.error):
            struct.Struct('@x')
        with self.assertRaises(struct.error):
            struct.Struct('@x')
        with
