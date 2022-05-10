import io
# Test io.RawIOBase

import unittest
import struct
import io
import sys

# A mixin defining tests common to RawIOBase, BufferedIOBase, and TextIOBase.
class CommonRawTestsMixin(object):
    def test_constructor(self):
        # No public constructor
        with self.assertRaises(TypeError):
            self.io.RawIOBase()

    def test_attributes(self):
        self.assertEqual(self.io.SEEK_SET, 0)
        self.assertEqual(self.io.SEEK_CUR, 1)
        self.assertEqual(self.io.SEEK_END, 2)
        self.assertEqual(self.io.DEFAULT_BUFFER_SIZE, io.DEFAULT_BUFFER_SIZE)

    def test_readinto(self):
        b = bytearray(self.stuff)
        n = self.io.RawIOBase.readinto(self.f, b)
        self.assertEqual(n, len(b))
