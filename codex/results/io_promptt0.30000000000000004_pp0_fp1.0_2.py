import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support
from test.support import os_helper

# A mixin for RawIOBase tests that are also valid for BufferedIOBase
class RawIOBaseMixin:
    def test_read_into(self):
        b = bytearray(10)
        n = self.io.readinto(b)
        self.assertEqual(n, len(self.data))
        self.assertEqual(b[:n], self.data)
        self.assertRaises(TypeError, self.io.readinto, memoryview(b))

    def test_readinto_array(self):
        b = bytearray(10)
        n = self.io.readinto(array.array('b', b))
        self.assertEqual(n, len(self.data))
        self.assertEqual(b[:n], self.data)

    def test_readinto_resize(self):
        b = bytearray(1)
        n =
