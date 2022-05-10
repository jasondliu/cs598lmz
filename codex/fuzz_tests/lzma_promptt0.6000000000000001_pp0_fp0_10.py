import lzma
# Test LZMADecompressor

class TestLZMADecompressor(unittest.TestCase):
    def test_small_input(self):
        # Issue #18282
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(b'\x01\x00\x00\x00'), b'')

    def test_decompress_incomplete(self):
        # Issue #18282
        d = lzma.LZMADecompressor()
        d.decompress(b'\x01\x00\x00')
        self.assertRaises(lzma.LZMAError, d.decompress, b'')

    def test_decompress_error(self):
        # Issue #18282
        d = lzma.LZMADecompressor()
        d.decompress(b'\x01\x00\x00\x00')
        self.assertRaises(lzma.LZMAError, d.decompress, b'\x01\
