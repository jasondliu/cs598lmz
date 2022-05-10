import lzma
# Test LZMADecompressor

class TestLZMADecompressor(unittest.TestCase):

    def test_decompress_extra_data(self):
        inp = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        decomp = lzma.LZMADecompressor()
        out = decomp.decompress(bytes(inp), max_length=5)
        self.assertEqual(out, bytes(5))
        self.assertEqual(decomp.unused_data, bytes(5))
        self.assertFalse(decomp.eof)

    def test_decompress_early_eof(self):
        inp = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        decomp = lzma.LZMADecompressor()
        out = decomp.decompress(bytes(inp
