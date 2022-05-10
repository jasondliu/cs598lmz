import lzma
# Test LZMADecompressor with valid data,
# and invalid data

# TODO: move this to test_lib_compress?

# note: the first test with valid data is also in test_lzma.py

import shutil
import sys
import types
import io

from test import support

class LZMADecompressorTestCase(unittest.TestCase):
    CHUNK = 1024

    def setUp(self):
        if shutil.which('xz') is None:
            self.skipTest('The xz utility is not available')
        f = open(support.findfile('xz-sample.txt'), mode='rb')
        self.data = f.read()
        f.close()

    def decompress(self, data):
        d = lzma.LZMADecompressor()
        res = []
        for c in [data[i:i + self.CHUNK] for i in range(0, len(data), self.CHUNK)]:
            r = d.decompress(c)
            if r:
                res.
