import lzma
# Test LZMADecompressor with a file-like object.

class TestLZMADecompressor(unittest.TestCase):

    def setUp(self):
        self.text = b"The quick brown fox jumps over the lazy dog."
        self.comp = lzma.LZMACompressor()
        self.data = self.comp.compress(self.text)
        self.data += self.comp.flush()

    def test_decompress(self):
        with io.BytesIO(self.data) as f:
            d = lzma.LZMADecompressor()
            self.assertEqual(d.decompress(f.read()), self.text)

    def test_unused_data(self):
        with io.BytesIO(self.data) as f:
            d = lzma.LZMADecompressor()
            self.assertEqual(d.decompress(f.read()), self.text)
            self.assertEqual(d.unused_data, b"")
        with io.BytesIO(self.
