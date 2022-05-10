import _struct
# Test _struct.Struct
import sys
import unittest
from test import test_support
import warnings

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('hHiIlLqQfd')
        self.assertEqual(s.size, 42)
        self.assertEqual(s.pack(1, 2, 3, 4, 5, 6, 7, 8, 9.0, 10.0),
                         '\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04'
                         '\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00'
                         '\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00'

