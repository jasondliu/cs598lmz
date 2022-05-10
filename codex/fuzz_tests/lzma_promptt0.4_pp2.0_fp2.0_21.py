import lzma
# Test LZMADecompressor

import io
import lzma
import unittest

from test import support
from test.support import bigmemtest


class TestLZMADecompressor(unittest.TestCase):

    def test_decompress_simple(self):
        # Test a simple round-trip through the decompressor.
        data = b"Hello"
        comp = lzma.compress(data)
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(comp), data)
        self.assertEqual(d.flush(), b"")

    def test_decompress_unused_data(self):
        # Test that unused_data is set correctly.
        data = b"Hello"
        comp = lzma.compress(data)
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(comp[:-1]), b"")
        self.assertEqual(d.unused_data, comp[-1:])
        self
