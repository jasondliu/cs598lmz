import _struct
# Test _struct.Struct.

import copy
import io
import sys
import struct
import unittest

import _testcapi

def tobytes(s):
    """Return a string of bytes from a unicode string"""
    if isinstance(s, str):
        return s
    return s.encode("latin-1")

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        self.assertEqual(struct.calcsize('i'), 4)
        self.assertEqual(struct.calcsize('ii'), 8)
        self.assertEqual(struct.calcsize('i'*100), 400)
        self.assertEqual(struct.calcsize('i'*1000), 4000)

    def test_unpack(self):
        self.assertEqual(struct.unpack('i', b'    '), (0,))
        self.assertEqual(struct.unpack('i', b'\x07\x5bCD')[0], 12345)
