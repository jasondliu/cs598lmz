import lzma
# Test LZMADecompressor

# Test that LZMADecompressor can decompress the data compressed with LZMA
# compressor.

import lzma
import os
import unittest

from test import support
from test.support import TESTFN, run_unittest, import_module

class LZMADecompressorTestCase(unittest.TestCase):

    def setUp(self):
        self.data = b"1234567890" * 100000
        self.compressor = lzma.LZMACompressor()

    def test_decompress(self):
        compressed = self.compressor.compress(self.data)
        compressed += self.compressor.flush()
        decompressor = lzma.LZMADecompressor()
        self.assertEqual(decompressor.decompress(compressed), self.data)

    def test_decompress_unused_data(self):
        compressed = self.compressor.compress(self.data)
        compressed += self.compressor.flush()
        compressed += b"abc"
       
