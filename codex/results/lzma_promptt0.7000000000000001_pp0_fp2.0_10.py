import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

class TestLZMA(unittest.TestCase):

    def test_LZMADecompressor(self):
        with lzma.open("tests/compressed_files/test_lzma.xz") as f:
            d= lzma.LZMADecompressor()
            data= d.decompress("".encode("utf-8"))
            self.assertEqual("LZMA test file\n", data.decode("utf-8"))

    def test_LZMACompressor(self):
        data="LZMA test file\n"
        c= lzma.LZMACompressor()
        compressed= c.compress(data.encode("utf-8"))
        c.flush()
        compressed += c.compress("".encode("utf-8"))
        d= lzma.LZMADecompressor()
        self.assertEqual(data, d.
