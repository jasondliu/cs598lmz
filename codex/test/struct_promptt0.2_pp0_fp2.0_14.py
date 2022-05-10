import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # Test struct.unpack()
        self.assertEqual(_struct.unpack('i', '\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.unpack('i', '\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.unpack('i', '\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.unpack('i', '\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.unpack('i', '\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.unpack('i', '\x01\x00\x00\x00'), (1,))
