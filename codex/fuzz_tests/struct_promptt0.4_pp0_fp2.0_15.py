import _struct
# Test _struct.Struct.unpack_from

import struct
import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_unpack_from(self):
        # test the .unpack_from() method
        s = _struct.Struct('i')
        buf = _struct.pack('i', 42)
        self.assertEqual(s.unpack_from(buf), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(memoryview(buf)), (42,))
        self.assertEqual(s.unpack_from(memoryview(buf), 0), (42,))
        self.assertRaises(struct.error, s.unpack_from, buf, 1)
        self.assertRaises(struct.error, s.unpack_from, buf, sys.maxsize)
        self.assertRaises(struct.error, s.unpack_from, memoryview(buf), 1)
        self
