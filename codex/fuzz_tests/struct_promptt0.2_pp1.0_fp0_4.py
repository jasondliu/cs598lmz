import _struct
# Test _struct.Struct.unpack_from

import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_unpack_from(self):
        s = _struct.Struct('i')
        buf = bytes(range(256))
        self.assertEqual(s.unpack_from(buf, 0), (0,))
        self.assertEqual(s.unpack_from(buf, 1), (1,))
        self.assertEqual(s.unpack_from(buf, 2), (2,))
        self.assertEqual(s.unpack_from(buf, 3), (3,))
        self.assertEqual(s.unpack_from(buf, 4), (4,))
        self.assertEqual(s.unpack_from(buf, 5), (5,))
        self.assertEqual(s.unpack_from(buf, 6), (6,))
        self.assertEqual(s.unpack_from(buf, 7), (7,))
        self.assertEqual(s.
