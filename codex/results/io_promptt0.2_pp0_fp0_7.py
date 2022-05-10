import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import bigmemtest

# A mixin class to test the readinto() method.
class ReadintoMixin:

    def test_readinto(self):
        b = bytearray(self.size)
        n = self.f.readinto(b)
        self.assertEqual(n, self.size)
        self.assertEqual(b, self.data)

    def test_readinto_non_empty(self):
        b = bytearray(self.size + 1)
        b[self.size] = 255
        n = self.f.readinto(b)
        self.assertEqual(n, self.size)
        self.assertEqual(b[:self.size], self.data)
        self.assertEqual(b[self.size], 255)

    def test_readinto_small_buffer(self):
        b = bytearray(self.size // 2)
        n = self.f.readinto(b)
        self.assertE
