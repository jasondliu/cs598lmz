import lzma
# Test LZMADecompressor

# Test the LZMADecompressor class

# This test is based on the LZMADecompressor test
# written by Nadeem Vawda.

import unittest
import io
import lzma

class TestLZMADecompressor(unittest.TestCase):

    def test_decompress(self):
        # Test decompression via the decompress() method.
        self.assertEqual(lzma.decompress(b''), b'')
        self.assertEqual(lzma.decompress(b'\x00'), b'')
        self.assertEqual(lzma.decompress(b'\x00\x00\x00\x00\x00'), b'')
        self.assertEqual(lzma.decompress(b'\x00\x00\x00\x00\x00\x04\x00'), b'\x00' * 4)
