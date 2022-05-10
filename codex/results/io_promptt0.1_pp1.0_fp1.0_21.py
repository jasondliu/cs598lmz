import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

# A mixin for RawIOBase subclasses that are implemented in terms of
# readinto() and write().
class ReadWriteTest:

    def test_read(self):
        self.assertEqual(self.read(0), b'')
        self.assertEqual(self.read(1), b'x')
        self.assertEqual(self.read(1), b'y')
        self.assertEqual(self.read(1), b'z')
        self.assertEqual(self.read(1), b'')

    def test_readall(self):
        self.assertEqual(self.readall(), b'xyz')

    def test_readinto(self):
        b = bytearray(b' ' * 10)
        n = self.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b[:3], b'xyz')
        self.assertEqual(self
