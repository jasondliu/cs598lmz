import lzma
# Test LZMADecompressor

# This test is based on the test test_lzma.py from Python 3.5.1

import unittest
from test import support

class CompressDecompressTestCase(unittest.TestCase):

    def test_decompressor(self):
        # Test that the decompressor accepts all of the valid input
        # formats.
        data = b'\x00' * 100
        for input_mode in ('contiguous', 'read', 'read1'):
            for output_mode in ('contiguous', 'read', 'read1'):
                with lzma.LZMADecompressor() as dec:
                    dec.decompress(data, input_mode, output_mode)
                with lzma.LZMADecompressor() as dec:
                    dec.decompress(data, input_mode)
                with lzma.LZMADecompressor() as dec:
                    dec.decompress(data)

        # Test that the decompressor raises errors for invalid input
        # formats.
        for input_mode in ('cont
