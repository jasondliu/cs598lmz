import lzma
# Test LZMADecompressor
class TestLZMADecompressor(unittest.TestCase):
    def test_LZMADecompressor_wrong_size(self):
        # Issue #3632: LZMADecompressor.decompress() should reject data
        # with a length that is not a multiple of 4
        compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ)
        data = compressor.compress(b"foo")
        data = data[:-1]
        decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
        with self.assertRaisesRegex(ValueError, 'Not a multiple of 4'):
            decompressor.decompress(data)

    def test_LZMADecompressor_wrong_size_stream(self):
        # Issue #3632: LZMADecompressor.decompress() should reject data
        # with a length that is not a multiple of 4
        compressor = lzma.LZMACompressor(format=
