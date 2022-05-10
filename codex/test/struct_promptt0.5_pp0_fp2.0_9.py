import _struct
# Test _struct.Struct()

# This test is not exhaustive.  Additional tests are in test_sre.py

import array
import _struct
import operator
import sys
import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')

    def test_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(s.unpack(b'\xff\xff\xff\xff'), (-1,))
