import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import _struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(1), struct.pack('i', 1))
        self.assertEqual(s.unpack(s.pack(1)), (1,))
        self.assertEqual(s.unpack_from(s.pack(1), 0), (1,))
        self.assertEqual(s.unpack_from(s.pack(1) + b'123', 0), (1,))
        self.assertEqual(s.unpack_from(s.pack(1) + b'123', 0, 1), (1,))
        self.assertEqual(s.unpack_from(s.pack(1) + b'123', 1), ())
        self.assertEqual(s.un
