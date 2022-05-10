import lzma
# Test LZMADecompressor

class TestLZMADecompressor(unittest.TestCase):
    def test_decompressor(self):
        # test that the decompressor can decompress a whole bunch of
        # data at once
        data = b"".join(b"test data %d" % i for i in range(10))
        comp = lzma.LZMACompressor()
        cdata = comp.compress(data)
        cdata += comp.flush()
        dcomp = lzma.LZMADecompressor()
        ddata = dcomp.decompress(cdata)
        self.assertEqual(data, ddata)

    def test_decompressor_with_trailing_garbage(self):
        data = b"".join(b"test data %d" % i for i in range(10))
        comp = lzma.LZMACompressor()
        cdata = comp.compress(data)
        cdata += comp.flush()
        cdata += b"garbage"
        dcomp = lzma.LZ
