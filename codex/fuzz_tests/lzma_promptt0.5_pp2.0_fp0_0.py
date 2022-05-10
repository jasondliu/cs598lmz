import lzma
# Test LZMADecompressor

# This is the same test as test_lzma.py, but it uses the LZMADecompressor
# class instead of the lzma module functions.

import unittest
import os
from io import BytesIO
from test import support

from lzma import LZMADecompressor, FORMAT_RAW, CHECK_NONE
from lzma import LZMAError, LZMA_MEMLIMIT_ERROR, LZMA_FORMAT_ERROR

TESTFN = support.TESTFN

class CompressDecompressTestCase(unittest.TestCase):
    def setUp(self):
        self.data = b"1234567890" * 1000

    def tearDown(self):
        support.unlink(TESTFN)

    def test_one_shot(self):
        # Test one-shot compression using a decompressor object.
        c = lzma.LZMACompressor()
        d = lzma.LZMADecompressor()
        b = c.compress(self.data)
