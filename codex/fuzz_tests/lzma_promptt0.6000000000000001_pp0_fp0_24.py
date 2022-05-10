import lzma
# Test LZMADecompressor.__init__(), LZMADecompressor.decompress(),
# LZMADecompressor.flush(), LZMADecompressor.copy()

class TestLZMADecompressor(unittest.TestCase):
    def test_init(self):
        # Test initializer.
        d = lzma.LZMADecompressor()
        self.assertEqual(d.eof, False)
        self.assertEqual(d.unused_data, b(""))
        self.assertEqual(d.decompress(b("")), b(""))

    def test_decompress_eof(self):
        # Test decompress() with EOF.
        d = lzma.LZMADecompressor()
        self.assertEqual(d.eof, False)
        self.assertEqual(d.unused_data, b(""))
        d.decompress(b("x"))
        self.assertEqual(d.eof, False)
        self.assertEqual(d.un
