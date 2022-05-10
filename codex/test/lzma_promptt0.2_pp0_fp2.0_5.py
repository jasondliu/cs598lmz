import lzma
# Test LZMADecompressor.decompress()

# This test is based on test_lzma.py from Python 3.4.2

import unittest
from test import support

class LZMADecompressorTestCase(unittest.TestCase):

    def test_decompress(self):
        # Test decompression of various data
        data = b'BZh91AY&SY\xd8\xcb\x97\x80'
        self.assertEqual(lzma.decompress(data), b'BZh91AY&SY\x99\xaf\xf2\x00')
        data = b'BZh91AY&SY\xd8\xcb\x97\x80' * 10
        self.assertEqual(lzma.decompress(data), b'BZh91AY&SY\x99\xaf\xf2\x00' * 10)
        data = b'BZh91AY&SY\xd8\xcb\x97\x80' * 100
