import lzma
# Test LZMADecompressor class

class LZMATest(unittest.TestCase):

    def test_decompressor(self):
        with open(TESTFN, 'wb') as f:
            f.write(b'a' * 10000)
        with open(TESTFN, 'rb') as f:
            c = lzma.compress(f.read())
        d = lzma.LZMADecompressor()
        with self.assertRaises(lzma.LZMAError):
            d.decompress(c)
        d.decompress(c[:1])
        d.decompress(c[1:])
        self.assertEqual(d.unused_data, b'')


class TestLZMACompressor(unittest.TestCase):

    def test_compressor(self):
        with open(TESTFN, 'wb') as f:
            f.write(b'a' * 10000)
        with open(TESTFN, 'rb') as f:
            c = lzma.LZMACompressor
