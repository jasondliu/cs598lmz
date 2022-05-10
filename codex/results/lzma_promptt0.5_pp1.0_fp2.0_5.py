import lzma
# Test LZMADecompressor
#
# This is a test for the LZMADecompressor class.
#
#

import unittest

from lzma import LZMADecompressor
from lzma import FORMAT_RAW, FORMAT_XZ, FORMAT_ALONE, FORMAT_AUTO

class LZMADecompressorTestCase(unittest.TestCase):
    def setUp(self):
        self.decompressor = LZMADecompressor()

    def test_decompress(self):
        # Test decompression of data compressed with xz.
        data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x04Hello world!\n'
        self.assertEqual(self.decompressor.decompress(data), b'Hello world!\n')
        self.assertEqual(self.decomp
