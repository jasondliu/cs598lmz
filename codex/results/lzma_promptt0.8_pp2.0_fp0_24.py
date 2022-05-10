import lzma
# Test LZMADecompressor class only

import unittest
from test.support import run_unittest, TESTFN

from lzma import LZMADecompressor, LZMACompressor, FORMAT_RAW


class LZMADecompressorTests(unittest.TestCase):

    @unittest.skipUnless(LZMADecompressor, "requires LZMADecompressor")
    def test_decompress(self):
        raw = b"12345678abcdef"

        c = LZMACompressor(FORMAT_RAW)
        lz = c.compress(raw)
        lz += c.flush()

        d = LZMADecompressor(FORMAT_RAW)
        self.assertEqual(d.decompress(lz), raw)

    @unittest.skipUnless(LZMADecompressor, "requires LZMADecompressor")
    def test_flush(self):
        raw = b"12345678"

        c = LZMACompressor(FORMAT_RAW)
        lz
