import _struct
# Test _struct.Struct.

import struct
import unittest

from test.support import run_unittest

class StructTestCase(unittest.TestCase):

    def test_struct(self):

        # Test _struct.Struct.

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.pack(-1), b'\xff\xff\xff\xff')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\xff\xff\xff\xff'), (-1,))
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.unpack)
