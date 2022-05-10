import lzma
# Test LZMADecompressor

class TestLZMADecompressor(unittest.TestCase):

    def test_decompress(self):
        with open(TESTFN, 'wb') as f:
            f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        with lzma.open(TESTFN, 'rb') as f:
            self.assertRaises(lzma.LZMAError, f.read)

    def test_decompressor_unused_data(self):
        with open(TESTFN, 'wb') as f:
            f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        with lzma.open(TESTFN, 'rb') as f:
            self.assertRaises(lzma.LZMAError, f.read)

    def test_decompressor_unused_data_eof(self):
        with
