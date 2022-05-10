import lzma
# Test LZMADecompressor boundary behavior.
from tests import test_support, test_lzma
from io import BytesIO

from lzma import *
from lzma.constants import *
from lzma.lzma_decompressor import *

import unittest


class LZMA_DecompressionTests(unittest.TestCase):
    def test_decompress(self):
        # LZMADecompressor.decompress() argument checking
        d = LZMADecompressor(FORMAT_RAW, memlimit=None)
        self.assertRaises(TypeError, d.decompress, 42)
        self.assertRaises(TypeError, d.decompress, '', 42)
        self.assertRaises(TypeError, d.decompress, '', True)
        self.assertRaises(ValueError, d.decompress, '', 0, -1)

    def test_max_length(self):
        d = LZMADecompressor(FORMAT_RAW)
        p = d.decompress(test
