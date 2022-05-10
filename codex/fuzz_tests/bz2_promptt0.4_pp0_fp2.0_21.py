import bz2
# Test BZ2Decompressor
#
# Note:
#   This is a test of the decompressor object, not the decompression
#   function.  The decompression function is tested in test_bz2.

from test import support
import unittest
import struct

class BZ2DecompressorTestCase(unittest.TestCase):
    def test_decompressor(self):
        # Test decompressor with multiple inputs and outputs
        data = bz2.compress(b'abcdeabcdeabcde')
        d = bz2.BZ2Decompressor()
        self.assertEqual(d.decompress(data[:4]), b'abcd')
        self.assertEqual(d.decompress(data[4:8]), b'eabc')
        self.assertEqual(d.decompress(data[8:12]), b'deab')
        self.assertEqual(d.decompress(data[12:]), b'cde')
        self.assertEqual(d.flush(), b'')

    def test_decompressor_flush(
