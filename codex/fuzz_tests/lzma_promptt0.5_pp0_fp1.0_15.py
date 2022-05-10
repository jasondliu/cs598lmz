import lzma
# Test LZMADecompressor

class LZMADecompressorTest(unittest.TestCase):
    def test_decompress(self):
        data = b'\x5d\x00\x00\x80\x00\x0bBZh91AY&SY\xad\xec\x80\x00\x00\x00\x00\x00\x00\x00\x00'
        expected = b'BZh91AY&SY\xad\xec\x80\x00\x00\x00\x00\x00\x00\x00\x00'
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(data), expected)
        self.assertEqual(d.unused_data, b'')

    def test_decompress_buffer(self):
        data = b'\x5d\x00\x00\x80\x00\x0bBZh91AY&SY\xad\xec\x80\x00\x
