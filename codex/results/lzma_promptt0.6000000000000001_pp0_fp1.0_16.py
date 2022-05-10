import lzma
# Test LZMADecompressor.read()

class TestLZMADecompressorRead(LZMADecompressorTestCase):

    def setUp(self):
        self.compressor = lzma.LZMADecompressor()
        self.set_compressor()
        self.data = b"x" * 100000
        self.compressed = self.compressor.compress(self.data)
        self.compressed += self.compressor.flush()

    def test_simple(self):
        read = self.decompressor.read()
        self.assertEqual(read, self.data)

    def test_read_0(self):
        read = self.decompressor.read(0)
        self.assertEqual(read, b"")

    def test_read_small(self):
        read = self.decompressor.read(1000)
        self.assertEqual(read, self.data[:1000])

    def test_read_partial(self):
        read = self.decompressor.read(1000)
        read += self.decomp
