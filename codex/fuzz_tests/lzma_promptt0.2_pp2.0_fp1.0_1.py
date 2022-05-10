import lzma
# Test LZMADecompressor

import io
import lzma
import unittest

from test import support

class LZMADecompressorTestCase(unittest.TestCase):

    def test_decompress(self):
        # Test decompression of various data sizes
        for i in range(0, 100):
            data = b'x' * i
            compressed = lzma.compress(data)
            d = lzma.LZMADecompressor()
            self.assertEqual(d.decompress(compressed), data)
            self.assertEqual(d.unused_data, b'')
            self.assertEqual(d.eof, True)

    def test_decompress_unused_data(self):
        # Test decompression with unused data
        data = b'x' * 100
        compressed = lzma.compress(data)
        compressed += b'abc'
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(compressed), data)
       
