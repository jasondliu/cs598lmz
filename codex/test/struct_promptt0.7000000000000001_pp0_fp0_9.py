import _struct
# Test _struct.Struct objects.

import unittest
from test import support
import struct

class StructTest(unittest.TestCase):
    def test_internal_size(self):
        class X(struct.Struct):
            _fmt = 'i'
        self.assertEqual(X.size, 4)
        self.assertEqual(X.__sizeof__(), 12)

    def test_unpack_from0(self):
        # SF buf 1647541: struct.unpack_from(fmt, buffer, offset=0) segfaults
        # See also http://bugs.python.org/issue1424152
        class S(struct.Struct):
            _fmt = 'i'
        data = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(S.unpack_from(data), (0,))
        self.assertEqual(S.unpack_from(data, 4), (0,))
