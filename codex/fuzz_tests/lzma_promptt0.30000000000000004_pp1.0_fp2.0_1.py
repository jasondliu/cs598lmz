import lzma
# Test LZMADecompressor.

# This is a test of the LZMADecompressor class.
# It is not a test of the lzma module.

import unittest
from test import support
from io import BytesIO

class LZMADecompressorTestCase(unittest.TestCase):

    def test_decompress(self):
        # Test decompression of a simple string.
        c = lzma.LZMADecompressor()
        self.assertEqual(c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00'), b'')
        self.assertEqual(c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x01'), b'')
        self.assertEqual(c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x02'), b'')
        self.assertEqual(c.decompress(b
