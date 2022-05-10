import _struct
# Test _struct.Struct().

import struct
import sys
import unittest
import _struct

from test import support

class StructTest(unittest.TestCase):

    def test_basics(self):
        S = _struct.Struct('...')
        self.assertEqual(S.size, 3)
        self.assertRaises(TypeError, S.pack, 0, 1, 2, 3)
        self.assertRaises(TypeError, S.pack)
        self.assertRaises(TypeError, S.pack, b'')
        self.assertRaises(TypeError, S.pack, 0, b'123')

        S = _struct.Struct('bBhHiIlLqQfd')
        self.assertEqual(S.size, struct.calcsize('bBhHiIlLqQfd'))

        S = _struct.Struct('hi')
        self.assertEqual(S.size, struct.calcsize('hi'))

        S = _struct.Struct('hhi')
