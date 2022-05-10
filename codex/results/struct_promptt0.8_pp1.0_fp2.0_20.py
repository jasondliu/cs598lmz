import _struct
# Test _struct.Struct.

import gc
import operator
import pickle
import sys
import unittest
from test import support

# Define a couple of struct's for testing.
test_struct = _struct.Struct('2s2s2s')
big_endian_test_struct = _struct.Struct('>3s3s3s')
little_endian_test_struct = _struct.Struct('<3s3s3s')

class StructTest(unittest.TestCase):
    def test_struct_format(self):
        self.assertEqual(test_struct.format, '<ccc')
        self.assertEqual(big_endian_test_struct.format, '>ccc')
        self.assertEqual(little_endian_test_struct.format, '<ccc')

    def test_unpack(self):
        self.assertEqual(test_struct.unpack(b'abcdefgh'), (b'ab', b'cd', b'ef'))
        self.assertEqual(big_endian_test_struct.un
