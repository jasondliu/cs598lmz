import io
# Test io.RawIOBase

import contextlib
import io
import unittest
from test import support

# A mixin class to add readinto() tests to IO tests
class ReadIntoMixin:

    def test_readinto(self):
        self.assertRaises(TypeError, self.IO.readinto)
        n = 1024
        b = bytearray(n)
        n = self.IO.readinto(b)
        self.assertEqual(n, len(self.FILE))
        self.assertEqual(b[:n], self.data)
        n = self.IO.readinto(b)
        self.assertEqual(n, 0)
        b = bytearray(n-1)
        self.assertRaises(ValueError, self.IO.readinto, b)
        self.assertRaises(TypeError, self.IO.readinto, memoryview(b'123'))

    def test_readinto_with_read(self):
        n = 1024
        b = bytearray(n)
        n = self.IO.read
