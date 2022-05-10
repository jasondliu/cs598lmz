import _struct
# Test _struct.Struct

import struct
import unittest

from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'abcd'), (1633837924,))
        self.assertEqual(s.unpack(b'abcd', 1), (1633837924,))
        self.assertEqual(s.unpack(b'abcd', 2), (1633837924,))
        self.assertEqual(s.unpack(b'abcd', 3), (1633837924,))
        self.assertEqual(s.unpack(b'abcd', 4), (1633837924,))
        self.assertEqual(s.unpack(b'abcd', 5), (1633837924,))
        self.assertEqual(s.unpack(b'abcd', 6), (1633837924,))
        self.assertEqual(s.unpack(b'abcd
