import lzma
# Test LZMADecompressor class.
#
# This is a test-only module, not intended for production use.
#
# Author: Daniel Stutzbach <daniel at stutzbachenterprises dot com>

import sys
import unittest

from test import support

class TestLZMADecompressor(unittest.TestCase):
    def check_decompress(self, decompressor, data, expected):
        self.assertEqual(decompressor.decompress(data), expected)
        self.assertEqual(decompressor.unused_data, b"")
        self.assertEqual(decompressor.eof, True)

    def test_decompress(self):
        # Test basic operation.
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(b""), b"")
        self.assertEqual(d.decompress(b"garbage"), b"")
        self.assertEqual(d.unused_data, b"garbage")
        self.assertE
