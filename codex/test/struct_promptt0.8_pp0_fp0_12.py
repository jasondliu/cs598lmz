import _struct
# Test _struct.Struct
try:
    import _struct
    _struct.Struct
except ImportError as e:
    raise ImportError("The _struct module is not built. If you want to import "
                      "array objects from Python code, then build _struct and "
                      "rebuild Python.")

from _testcapi import INT_MAX, INT_MIN
from _testcapi import cast_long

import unittest

import sys
import io

from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), '\x01\x00\x00\x00')
        self.assertEqual(s.pack(-1), '\xff\xff\xff\xff')
        self.assertEqual(s.pack(0x76543210), '\x10\x32\x54\x76')
