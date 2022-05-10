import lzma
# Test LZMADecompressor.decompress()

# This test is based on the test_lzma.py test_decompress() test
# from the Python 3.4.2 standard library.

# The original test was written by Nadeem Vawda.

import unittest

from lzma import LZMADecompressor

class LZMADecompressorTest(unittest.TestCase):

    def test_decompress(self):
        # Test decompression of a single-byte stream.
        d = LZMADecompressor()
        self.assertEqual(d.decompress(b"\x00"), b"")
        self.assertEqual(d.decompress(b"\x00\x00"), b"")
        self.assertEqual(d.decompress(b"\x00\x00\x00"), b"")
        self.assertEqual(d.decompress(b"\x00\x00\x00\x00"), b"")
