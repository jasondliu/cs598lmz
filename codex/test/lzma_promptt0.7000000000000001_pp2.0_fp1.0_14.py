import lzma
# Test LZMADecompressor.input()

# Test for segfault: https://bugs.python.org/issue36131
# Also, test that feeding a small buffer will work

# Note: this test uses only a small buffer size to test that
# LZMAFile.read(size=n) works correctly.

# This test is based on lzma.LZMAFile.test.test_readline()

from io import BytesIO
import pickle
import unittest
from test import support

class LZMADecompressorInputTest(unittest.TestCase):

    def setUp(self):
        f = self.f = BytesIO()
        f.write(b'x' * 1024)
        f.seek(0)
        self.lz = lzma.LZMADecompressor()

    def tearDown(self):
        self.f.close()

    def feed(self, s):
        # Return a byte string created by feeding the string s to
        # the decompressor.
        self.lz.input(s)
