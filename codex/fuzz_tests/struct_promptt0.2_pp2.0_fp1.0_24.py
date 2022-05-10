import _struct
# Test _struct.Struct.

import struct
import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        self.assertEqual(_struct.unpack('i', b'abcd'), (1633837924,))
        self.assertEqual(_struct.unpack('i', b'abcd', 0), (1633837924,))
        self.assertEqual(_struct.unpack('i', b'abcd', 1), (1684234849,))
        self.assertEqual(_struct.unpack('i', b'abcd', 2), (1684890117,))
        self.assertEqual(_struct.unpack('i', b'abcd', 3), (1668246573,))
        self.assertEqual(_struct.unpack('i', b'abcd', 4), (1768842341,))
        self.assertEqual(_struct.unpack('i', b'abcd', -1), (1768842341,))
        self.assertE
