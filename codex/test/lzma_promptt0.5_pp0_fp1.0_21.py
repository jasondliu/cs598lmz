import lzma
# Test LZMADecompressor

# Note: This test is based on the tests for BZ2Decompressor
# in Lib/test/test_bz2.py

import unittest
from test import support
from io import BytesIO

class TestLZMADecompressor(unittest.TestCase):

    def setUp(self):
        self.decompressor = lzma.LZMADecompressor()

