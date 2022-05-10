import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_format_size_alignment(self):
        # Issue #7995: check that the format string is correct.
        for format in 'bBhHiIlLqQfd':
            s = _struct.Struct(format)
            self.assertEqual(s.size, s.size)
            self.assertEqual(s.format, format)

    def test_unpack_from(self):
        # Issue #7995: check that unpack_from() can take a buffer.
        s = _struct.Struct('i')
        buf = bytes(bytearray(range(256)))
        self.assertEqual(s.unpack_from(buf, 0), (0,))
        self.assertEqual(s.unpack_from(buf, 128), (50462976,))

    def test_pack_into(self):
        # Issue #7995: check that pack_into() can take a buffer.
        s = _
