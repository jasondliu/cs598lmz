import lzma
# Test LZMADecompressor works properly.
class TestLZMADecompressor(DecompressorTestCase):
    def setUp(self) -> None:
        self.x = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
    def test_decompress_xz(self) -> None:
        self.assertEqual(self.decompress(b'\xfd7zXZ\0'), b'')
