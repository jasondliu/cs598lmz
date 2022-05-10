import _struct
# Test _struct.Struct

# Simple tests, using the standard struct module
# to check our results.

import struct as std
from test.support import run_unittest
import unittest
import sys

class StructTest(unittest.TestCase):

    def test_format(self):
        # Test struct.format
        s = _struct.Struct('abc')
        self.assertEqual(s.format, 'abc')
        s = _struct.Struct('!abc')
        self.assertEqual(s.format, '!abc')
        s = _struct.Struct('abcdef')
        self.assertEqual(s.format, 'abcdef')
        s = _struct.Struct('abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(s.format, 'abcdefghijklmnopqrstuvwxyz')
        s = _struct.Struct('@abc')
        self.assertEqual(s.format, 'abc')
        s = _struct.Struct('=abc')
