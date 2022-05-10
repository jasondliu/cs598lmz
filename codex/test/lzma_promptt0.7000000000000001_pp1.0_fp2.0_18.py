import lzma
# Test LZMADecompressor with read() calls of various sizes.
# This exercises the internal buffering code.

import unittest
from test import support
from io import BytesIO

class TestLZMAread(unittest.TestCase):

    def setUp(self):
        self.x = lzma.compress(b'a' * 1000)

    def test_read_one(self):
        d = lzma.LZMADecompressor()
        f = BytesIO(self.x)
        decomp = d.decompress(f.read(1))
        self.assertEqual(decomp, b'')
        self.assertEqual(d.unconsumed_tail, b'')
        decomp = d.decompress(f.read())
        self.assertEqual(decomp, b'a' * 1000)
        self.assertEqual(d.unconsumed_tail, b'')

def test_main():
    support.run_unittest(TestLZMAread)

