import lzma
# Test LZMADecompressor

# Test the LZMADecompressor class.

# This test checks the basic functionality of the LZMADecompressor class.
# It is not intended to catch all errors.

# XXX: This test is incomplete.

import io
import unittest
import lzma

class TestLZMADecompressor(unittest.TestCase):
    def test_decompressor(self):
        # Test the decompressor object
        d = lzma.LZMADecompressor()
        self.assertEqual(d.eof, False)
        self.assertEqual(d.unused_data, b"")
        self.assertEqual(d.decompress(b""), b"")
        self.assertEqual(d.eof, False)
        self.assertEqual(d.unused_data, b"")
        self.assertRaises(lzma.LZMAError, d.decompress, b"\x00")
        self.assertEqual(d.eof, False)
        self
