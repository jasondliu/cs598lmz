import lzma
# Test LZMADecompressor with all inputs on the edge of error conditions.


class CompatibleTestCase(unittest.TestCase):
    def test_already_decompressed_error(self):
        m = lzma.LZMADecompressor()
        with self.assertRaisesRegex(lzma.LZMAError,
            'Compressed data ended before the end-of-stream marker was reached'):
            m.decompress(b'foobar')

    def test_error_after_eof(self):
        m = lzma.LZMADecompressor()
        with self.assertRaisesRegex(lzma.LZMAError,
            'Compressed data ended before the end-of-stream marker was reached'):
            m.decompress(b'Y\xbam\x01\x00\x04\x00\x00\x00\x80\x00\x00\x8c\xef\xf2o'
                )

    def test_magic_error(self):
        m = lzma.LZM
