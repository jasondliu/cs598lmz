import lzma
# Test LZMADecompressor

# Test LZMADecompressor

import unittest
import io
import os
import lzma

from test import support

class LZMADecompressorTestCase(unittest.TestCase):

    def test_decompress(self):
        data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
        decomp = lzma.LZMADecompressor()
        self.assertEqual(decomp.decompress(data), b'hello')
        self.assertEqual(decomp.unused_data, b'')
        self.assertEqual(decomp.decompress(b''), b'')
        self.assertEqual(decomp.unused_data, b'')
        self.assertEqual(decomp.decompress(b'w'), b'')
        self.
