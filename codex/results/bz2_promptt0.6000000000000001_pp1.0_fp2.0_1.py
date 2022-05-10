import bz2
# Test BZ2Decompressor for decompression
import io
import os
import sys
import unittest
from test import support

try:
    import zlib
except ImportError:
    zlib = None


class BaseTest(unittest.TestCase):
    decompressobj = bz2.BZ2Decompressor
    input_size = 1024

    def setUp(self):
        self.data = bz2.compress(b'a' * self.input_size)

    def decompress(self, data):
        d = self.decompressobj()
        return d.decompress(data)

    def test_decompress(self):
        for i in range(256):
            d = self.decompressobj()
            self.assertEqual(d.decompress(self.data[:i]), b'a' * i)
            self.assertEqual(d.unused_data, self.data[i:])

    def test_flush(self):
        d = self.decompressobj()
        self.assertEqual(d.decompress
