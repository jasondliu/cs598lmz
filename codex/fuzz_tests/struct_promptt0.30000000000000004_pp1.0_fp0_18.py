import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct_unpack(self):
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self
