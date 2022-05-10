import lzma
# Test LZMADecompressor and LZMACompressor classes.

import unittest
from test import support

class CompressorTestCase(unittest.TestCase):

    def test_all_algorithms(self):
        """Test all algorithms with LZMACompressor()"""
        for flavor in range(2):
            for preset in (0, 1, 9):
                comp = lzma.LZMACompressor(
                    format=lzma.FORMAT_XZ,
                    check=-1,
                    preset=preset,
                    filters=[
                        {"id": lzma.FILTER_LZMA2, "dict_size": 4096,
                         "lc": 3, "lp": 0, "pb": 2,
                         "mode": lzma.MODE_NORMAL,
                         "nice_len": 64, "mf": lzma.MF_HC4,
                         "depth": 0},
                        {"id": lzma.FILTER_DELTA, "dist": 2},
                        {"id": lzma.FILTER_DELTA, "dist": 2},
                    ],
