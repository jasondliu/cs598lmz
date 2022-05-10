import bz2
# Test BZ2Decompressor
#
# This test is not very thorough, but it does test that the BZ2Decompressor
# class is working.

import bz2
import io
import unittest
import zlib

from test import support

class TestBZ2Decompressor(unittest.TestCase):
    def test_decompressor(self):
        # Test BZ2Decompressor with various inputs.
        data = bz2.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0'
                            b'\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe'
                            b'\x084')
        d = bz2.BZ2Decompressor()
        self.assertEqual(d.decompress(data), b'BZh91AY&SY\x94$|\x0e\x00\x00\
