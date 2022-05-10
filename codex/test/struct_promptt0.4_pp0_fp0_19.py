import _struct
# Test _struct.Struct.__reduce__()
import pickle
import sys
import unittest
from test import support

try:
    import _testcapi
except ImportError:
    _testcapi = None

class StructTestCase(unittest.TestCase):
    def test_basics(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00', 0), (1,))
        self.assertE
