import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # Test struct.unpack()
        self.assertEqual(_struct.unpack('i', b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.unpack('i', b'\x00\x00\x00\x01'), (1,))
        self.assertEqual(_struct.unpack('i', b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.unpack('i', b'\x00\x00\x00\x01'), (1,))
        self.assertEqual(_struct.unpack('i', b'\x00\x00\x00\x01'), (1,))
        self.assertEqual(_struct.unpack('i', b'\x01\x00\x00\x00'), (1,))
