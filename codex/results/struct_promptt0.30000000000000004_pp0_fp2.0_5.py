import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct objects

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')

        s = _struct.Struct('hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.format, 'hhl')

        # test struct unpacking
        for (fmt, input, output) in (
            ('bbbb', b'abcd', [97, 98, 99, 100]),
            ('hhhh', b'abcd', [25185, 25699, 25700, 26213]),
            ('ii', b'abcd', [1633837924, 1701192660]),
            ('ll', b'abcd', [1633837924, 1701192660]),
            ('qq', b'abcd', [1633837924, 1701192660]),

