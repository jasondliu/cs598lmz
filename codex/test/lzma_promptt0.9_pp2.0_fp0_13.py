import lzma
# Test LZMADecompressor and LZMACompressor classes.

import unittest
from test import support

class CompressorTestCase(unittest.TestCase):

    def test_all_algorithms(self):
        """Test all algorithms with LZMACompressor()"""
