import lzma
# Test LZMADecompressor
class LZMADecompressorTest(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(lzma.LZMADecompressor()), lzma.LZMADecompressor)

    def test_decompress(self):
        with lzma.open('lzma.test', mode='rb') as comp_file:
            comp_data = comp_file.read()
        decomp = lzma.LZMADecompressor()
        self.assertEqual(decomp.decompress(comp_data),
                         b'This is some text. It is not very long. ')
        self.assertEqual(decomp.unused_data, b'')
        self.assertEqual(decomp.eof, True)
        # The input is truncated.
        decomp = lzma.LZMADecompressor()
        self.assertRaises(lzma.LZMAError, decomp.decompress,
                          comp_data[:len(comp_
