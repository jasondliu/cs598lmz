import _struct
# Test _struct.Struct

import struct
import unittest

from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # test struct.unpack
        self.assertEqual(struct.unpack('i', '\x00\x00\x00\x00'), (0,))
        self.assertEqual(struct.unpack('i', '\x01\x00\x00\x00'), (1,))
        self.assertEqual(struct.unpack('i', '\x00\x01\x00\x00'), (256,))
        self.assertEqual(struct.unpack('i', '\x00\x00\x01\x00'), (65536,))
        self.assertEqual(struct.unpack('i', '\x00\x00\x00\x01'), (16777216,))
        self.assertEqual(struct.unpack('i', '\xff\xff\xff\xff'), (-1,))
        self.assertEqual
