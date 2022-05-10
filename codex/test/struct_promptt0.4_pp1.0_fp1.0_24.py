import _struct
# Test _struct.Struct

import sys
import _struct
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.unpack(b'abcd'), (1633837924,))
        self.assertEqual(s.unpack(b'efgh'), (1701011303,))
        self.assertRaises(TypeError, s.unpack, 42)
        self.assertRaises(TypeError, s.unpack, 'abcdefgh')
        self.assertRaises(TypeError, s.unpack, b'abcdefgh')
        self.assertRaises(struct.error, s.unpack, b'ab')
        self.assertRaises(struct.error, s.unpack, b'abc')
        self.assertRaises(struct.error, s.unpack, b'abcdab')
