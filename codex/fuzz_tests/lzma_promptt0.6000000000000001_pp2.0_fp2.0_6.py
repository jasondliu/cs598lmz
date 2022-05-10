import lzma
# Test LZMADecompressor
class TestLZMADecompressor(TestCase):
    def test_decompressor(self):
        d = lzma.LZMADecompressor()
        data = d.decompress(b'\x00\x00\x00\x03\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(data, b'\x00')
        self.assertEqual(d.unused_data, b'')
        self.assertEqual(d.eof, True)
        data = d.decompress(b'\x00\x00\x00\x09\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00
