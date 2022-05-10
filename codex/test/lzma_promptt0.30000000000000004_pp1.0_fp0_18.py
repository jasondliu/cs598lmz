import lzma
# Test LZMADecompressor

import io
import lzma
import os
import unittest

from test import support

class LZMADecompressorTestCase(unittest.TestCase):

    def test_decompress(self):
        with support.check_warnings(("", DeprecationWarning)):
            decomp = lzma.LZMADecompressor()
        self.assertRaises(TypeError, decomp.decompress)
        self.assertRaises(ValueError, decomp.decompress, b"")
        self.assertRaises(ValueError, decomp.decompress, b"\x00")
        self.assertRaises(ValueError, decomp.decompress, b"\x00" * 5)
        self.assertRaises(ValueError, decomp.decompress, b"\x00" * 13)
        self.assertRaises(ValueError, decomp.decompress, b"\x00" * 14)
        self.assertRaises(ValueError, decomp.decompress, b"\x00" * 15)
