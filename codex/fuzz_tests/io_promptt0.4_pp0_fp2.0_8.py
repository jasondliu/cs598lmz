import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import unittest
from test import support

class TestReadinto(unittest.TestCase):

    def setUp(self):
        self.f = io.BytesIO(b"abc")

    def test_readinto(self):
        b = bytearray(2)
        n = self.f.readinto(b)
        self.assertEqual(n, 2)
        self.assertEqual(b, b"ab")
        self.assertEqual(self.f.tell(), 2)

    def test_readinto_resize(self):
        b = bytearray(1)
        n = self.f.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(b, b"a")
        self.assertEqual(self.f.tell(), 1)

    def test_readinto_non_writeable(self):
        b = memoryview(bytearray(2))
        self.assertRaises(TypeError
