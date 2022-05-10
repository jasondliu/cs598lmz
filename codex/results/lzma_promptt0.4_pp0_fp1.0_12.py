import lzma
# Test LZMADecompressor

class TestLZMADecompressor(unittest.TestCase):

    def test_decompress_returns_bytes(self):
        data = b'\x00'
        c = lzma.LZMADecompressor()
        self.assertEqual(c.decompress(data), b'')

    def test_flush_returns_bytes(self):
        data = b'\x00'
        c = lzma.LZMADecompressor()
        self.assertEqual(c.flush(), b'')

    def test_decompress_with_max_length(self):
        c = lzma.LZMADecompressor()
        self.assertRaises(ValueError, c.decompress, b'', max_length=0)
        self.assertRaises(ValueError, c.decompress, b'', max_length=-1)
        self.assertRaises(ValueError, c.decompress, b'', max_length=1)
        self.assertEqual(c.
