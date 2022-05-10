import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('P')
        with self.assertRaises(TypeError):
            _struct.Struct('P', None)
        with self.assertRaises(TypeError):
            _struct.Struct('P', 'abc')
        with self.assertRaises(TypeError):
            _struct.Struct('P', 'abc', None)
        with self.assertRaises(TypeError):
            _struct.Struct('P', 'abc', 'def')
        with self.assertRaises(TypeError):
            _struct.Struct('P', 'abc', 'def', None)
        with self.assertRaises(TypeError):
            _
