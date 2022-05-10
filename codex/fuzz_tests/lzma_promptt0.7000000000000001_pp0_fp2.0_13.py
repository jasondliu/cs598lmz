import lzma
# Test LZMADecompressor object for decompressing data incrementally.

from test import support
from test.support import run_unittest

from io import BytesIO
from lzma import LZMADecompressor
from lzma import LZMAError, LZMA_FORMAT_ERROR
from lzma import FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE

try:
    LZMADecompressor().decompress(b'')
except NotImplementedError:
    raise unittest.SkipTest("requires a working LZMADecompressor.decompress()")

class IncrementalDecompressorTestCase(unittest.TestCase):
    data = b'The quick brown fox jumps over the lazy dog.'

    def test_decompress(self):
        # Decompress with an LZMADecompressor object.
        compressor = LZMADecompressor()
        f = BytesIO()
        for c in [compressor.compress(self.data[:16]),
                  compressor.compress(self.data[16
