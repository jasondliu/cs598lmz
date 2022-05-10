import lzma
# Test LZMADecompressor objects

class LZMADecompressorTest(unittest.TestCase):

    data1 = b"".join([(x+y).encode()
        for x,y in zip(ascii_lowercase, ascii_uppercase)])

    def test_decompressor_attributes(self):
        c = lzma.LZMADecompressor()
        self.assertEqual(c.eof, 0)
        c = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
        self.assertEqual(c.format, lzma.FORMAT_RAW)
        c = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
        self.assertEqual(c.format, lzma.FORMAT_XZ)
        self.assertRaises(ValueError, lzma.LZMADecompressor, format=12345)
        c = lzma.LZMADecompressor(filters=[])
       
