import lzma
# Test LZMADecompressor

# Test LZMADecompressor

class TestLZMADecompressor(unittest.TestCase):
    def test_decompress(self):
        data = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(
            lzma.LZMADecompressor().decompress(data),
            b''
        )

    def test_decompress_error(self):
        data = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        with self.assertRaises(lzma.LZMAError):
            lzma.LZMADecompressor().decompress(data, max_length=0)

    def test_decompress_unused_data(self):
        data = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(
            lzma.
