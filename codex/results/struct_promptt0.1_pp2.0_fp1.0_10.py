import _struct
# Test _struct.Struct.

import struct
import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # Test _struct.Struct.unpack().
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00', 0), (1,))
        self.assertEqual(s.unpack(b'xx\x01\x00\x00\x00xx', 2), (1,))
        self.assertEqual(s.unpack(memoryview(b'\x01\x00\x00\x00')), (1,))
        self.assertEqual(s.unpack(memoryview(b'\x01\x00\x00\x00'), 0), (1,))
        self.assertEqual(s.unpack(memory
