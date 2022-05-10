import _struct
# Test _struct.Struct.

import operator
import struct
import sys
import unittest
from test import support, test_struct

class StructTest(unittest.TestCase):
    def setUp(self):
        self.fmt = 'hhl'
        self.s = _struct.Struct(self.fmt)

    def test_basics(self):
        self.assertEqual(self.s.format, self.fmt)
        self.assertEqual(self.s.size, struct.calcsize(self.fmt))
        self.assertEqual(self.s.pack(1, 2, 3),
                         struct.pack(self.fmt, 1, 2, 3))
        self.assertEqual(self.s.unpack(self.s.pack(1, 2, 3)), (1, 2, 3))
        self.assertEqual(self.s.unpack_from(self.s.pack(1, 2, 3), 0),
                         (1, 2, 3))
        self.assertEqual(self.s.unpack_from(self
