import _struct
# Test _struct.Struct
import unittest
from test import test_support
import sys
import copy

def roundtrip(s, v):
    return s.unpack(s.pack(*v))

class StructTest(unittest.TestCase):
    def test_bool(self):
        s = _struct.Struct('?')
        for v in (0, 1):
            self.assertEqual(roundtrip(s, (v,)), (v,))
        for v in (-1, 2):
            self.assertRaises(struct.error, s.pack, v)

    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')

    def test_unpack_from(self):
        # Test unpacking from a buffer
        s = _struct.Struct('i')
        buf = buffer('\x01\x02\x03\x04')
