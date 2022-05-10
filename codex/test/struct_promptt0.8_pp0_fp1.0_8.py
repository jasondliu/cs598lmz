import _struct
# Test _struct.Struct with standard defaults
import unittest
import os
from test import support

class StructTestCase(unittest.TestCase):
    def setUp(self):
        self.s = _struct.Struct("i")

    def test_size(self):
        self.assertEqual(self.s.size, 4)

    def test_pack(self):
        self.assertEqual(self.s.pack(42), b'*\x00\x00\x00')

    def test_unpack(self):
        self.assertEqual(self.s.unpack(b'*\x00\x00\x00'), (42,))

    def test_pack_unpack(self):
        for i in range(1000):
            self.assertEqual(self.s.unpack(self.s.pack(i))[0], i)

