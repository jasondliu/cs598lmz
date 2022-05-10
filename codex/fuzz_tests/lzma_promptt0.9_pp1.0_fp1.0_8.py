import lzma
# Test LZMADecompressor and LZMACompressor
# These tests were ported from test/test_lzma.py in CPython 3.2
MAX_COPY = 65536
INBUFSIZ = 200 * 1024

class BaseTest(unittest.TestCase):
    def get_good_decompressor(self):
        return lzma.LZMADecompressor()

    def get_good_compressor(self, format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=None):
        return lzma.LZMACompressor(format=format, check=check, preset=preset)

    def get_bad_compressor(self):
        raise NotImplementedError

class BadOpenTest(BaseTest):
    @unittest.skip("lzma module is not able to check the lzma stream format.")
    def test_bad_open(self):
        self.assertRaises(ValueError, lzma.LZMADecompressor, format=lzma.FORMAT_ALONE)
       
