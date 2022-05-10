import _struct
# Test _struct.Struct.pack_into()

import sys
import unittest

from test import support

class StructTest(unittest.TestCase):

    def test_pack_into(self):
        # Issue #16234.
        s = _struct.Struct('i')
        buf = bytearray(s.size)
        s.pack_into(buf, 0, 1)
        self.assertEqual(s.unpack_from(buf, 0), (1,))
        buf = bytearray(s.size + 1)
        s.pack_into(buf, 1, 1)
        self.assertEqual(s.unpack_from(buf, 1), (1,))
        buf = bytearray(s.size * 2)
        s.pack_into(buf, s.size, 1)
        self.assertEqual(s.unpack_from(buf, s.size), (1,))

    def test_unpack_from(self):
        # Issue #16234.
        s = _struct.Struct('i')
