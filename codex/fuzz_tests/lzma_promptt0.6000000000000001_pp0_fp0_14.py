import lzma
# Test LZMADecompressor for bad input
#
# This test checks that LZMADecompressor raises an error when given
# incomplete input data.

import io

from test.support import run_unittest

from test.test_lzma import CompressBufferTest, DecompressBufferTest, \
    DecompressFileTest, DecompressFileTextTest, DecompressFileSeekTest


class LZMADecompressorBadInputTest(CompressBufferTest):

    def test_bad_input(self):
        for input in (b'', b'\x00', b'\x00\x00', b'\x00\x00\x00\x00',
                      b'\x00\x00\x00\x00\x00\x00\x00\x00'):
            self.assertRaises(lzma.LZMAError, self.decompress, input)

    def test_bad_eof(self):
        self.assertRaises(lzma.LZMAError, self.decompress,
                          self.compress
