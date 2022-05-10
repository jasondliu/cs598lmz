import _struct
# Test _struct.Struct.

from test import support
import unittest
from array import array
from _testcapi import INT_MAX, INT_MIN

class StructTestCase(unittest.TestCase):

    def test_bool(self):
        # Issue #1702: bool is not supported as a struct format code.
        self.assertRaises(TypeError, _struct.Struct, '?')

    def test_unpack_from(self):
        # Test the optional buffer related functionality
        s = _struct.Struct('i')
        buf = array('b', [0, 0, 0, 0])
        self.assertEqual(s.unpack_from(buf, 0), (0,))
        self.assertEqual(s.unpack_from(buf, 1), (0,))
        self.assertEqual(s.unpack_from(buf, 2), (0,))
        self.assertEqual(s.unpack_from(buf, 3), (0,))
        self.assertRaises(struct.error, s.unpack_from, buf, 4)

