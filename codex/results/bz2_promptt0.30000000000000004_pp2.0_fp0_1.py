import bz2
# Test BZ2Decompressor
#
# Test the BZ2Decompressor class directly.

import bz2
import io
import unittest

from test import test_support

class TestBZ2Decompressor(unittest.TestCase):

    def test_decompress(self):
        # Test decompression of various blocksizes.
        #
        # The bz2 module doesn't expose the blocksize, so we have to
        # decompress the data and check the length.
        for blocksize in xrange(1, 1025, 111):
            compressor = bz2.BZ2Compressor(blocksize)
            data = compressor.compress(b"foo") + compressor.flush()
            self.assertEqual(len(data), blocksize + 1)
            decompressor = bz2.BZ2Decompressor()
            self.assertEqual(decompressor.decompress(data), b"foo")
            self.assertEqual(decompressor.unused_data, b"")

    def test_unused_data(self):
        # Test that unused_
