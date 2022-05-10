import _struct
# Test _struct.Struct and _struct.unpack_from

import array
from test import support
import unittest

class StructTestCase(unittest.TestCase):
    def test_unpack_from(self):
        s = _struct.Struct('i')
        a = array.array('b', [0,0,0,0, 0,0,0,1, 0,0,0,2])
        self.assertEqual(s.unpack_from(a, 0), (0,))
        self.assertEqual(s.unpack_from(a, 4), (1,))
        self.assertEqual(s.unpack_from(a, 8), (2,))
        self.assertRaises(struct.error, s.unpack_from, a, 12)
        self.assertRaises(struct.error, s.unpack_from, a, 13)
        self.assertRaises(struct.error, s.unpack_from, a, -1)

