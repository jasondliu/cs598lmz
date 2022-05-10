import lzma
# Test LZMADecompressor and LZMACompressor classes

# This test assumes that the underlying lzma library is working properly,
# and only tests the Python interface.

import unittest
from test import support
from io import BytesIO

class TestLZMA(unittest.TestCase):
    def test_decompressor(self):
        # Test basic functions of the LZMADecompressor class.
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(b''), b'')
        self.assertEqual(d.unused_data, b'')
        self.assertEqual(d.eof, False)

        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(b'x'), b'x')
        self.assertEqual(d.unused_data, b'')
        self.assertEqual(d.eof, False)

        data = b'1234567890' * 10000
        c = lzma.L
