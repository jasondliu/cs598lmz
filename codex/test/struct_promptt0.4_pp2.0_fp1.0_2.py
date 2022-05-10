import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTest(unittest.TestCase):

    def test_unpack(self):
        # Test the unpack method.
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'*2), (1, 1))
        self.assertRaises(struct.error, s.unpack, b'')
        self.assertRaises(struct.error, s.unpack, b'\x01\x00\x00')

    def test_unpack_from(self):
        # Test the unpack_from method.
        s = _struct.Struct('i')
