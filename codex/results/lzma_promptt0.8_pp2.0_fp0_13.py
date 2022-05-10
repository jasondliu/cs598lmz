import lzma
# Test LZMADecompressor objects

from test import support
import unittest
import io
from lzma import LZMADecompressor

TEST_DATA = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x95\x19\xe0\x0f\x89\xc1\xd1,\x10\x04\x9d\x11\x04\x01BA\x01P\xa0\x0e:\x06\x06\x02\x00\x00\x00\x04\x00\x00\x00\x00'

class LZMADecompressTestCase(unittest.TestCase):

    def test_decompress_valid_data(self):
        # Test valid compressed data
        data = 'LZMA compressed data'
        cdata = TEST_DATA
        self.assertEqual(data, LZMADecompressor().decomp
