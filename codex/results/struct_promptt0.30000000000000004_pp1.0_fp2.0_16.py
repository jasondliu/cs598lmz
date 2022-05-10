import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct objects
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.pack(12345), struct.pack('i', 12345))
        self.assertEqual(s.unpack(s.pack(12345)), (12345,))
        self.assertEqual(s.unpack_from(s.pack(12345), 0), (12345,))
        self.assertEqual(s.unpack_from(s.pack(12345), 1), ())
        self.assertEqual(s.unpack_from(s.pack(12345), 2), ())
        self.assertEqual(s.unpack_from(s.pack(12345), 3), ())
        self.assertE
