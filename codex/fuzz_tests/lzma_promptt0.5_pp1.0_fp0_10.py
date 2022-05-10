import lzma
# Test LZMADecompressor.decompress()

class TestLZMADecompressor(unittest.TestCase):
    def test_decompress_1(self):
        # Test decompressing a single byte
        c = lzma.LZMADecompressor()
        self.assertEqual(c.decompress(b"\x00"), b"")
        self.assertEqual(c.decompress(b"\x00\x00"), b"")
        self.assertEqual(c.decompress(b"\x00\x00\x00"), b"")
        self.assertEqual(c.decompress(b"\x00\x00\x00\x00"), b"")
        self.assertEqual(c.decompress(b"\x00\x00\x00\x00\x00"), b"")
        self.assertEqual(c.decompress(b"\x00\x00\x00\x00\x00\x00"), b"")
        self.assertEqual(c.dec
