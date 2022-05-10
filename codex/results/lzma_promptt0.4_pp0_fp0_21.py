import lzma
# Test LZMADecompressor
#
# The LZMA file format is a container format.  This test only tests
# the raw LZMA stream decompressor.
#
# The test vectors are from the LZMA SDK 4.32 (lzma432.zip).

class TestLZMADecompressor:
    def test_decompress(self):
        for i in range(1, 9):
            with open(os.path.join(os.path.dirname(__file__),
                                   'lzma_data/e' + str(i)), 'rb') as f:
                data = f.read()
            with open(os.path.join(os.path.dirname(__file__),
                                   'lzma_data/d' + str(i)), 'rb') as f:
                expected = f.read()
            d = lzma.LZMADecompressor()
            res = d.decompress(data)
            assert res == expected


class TestLZMADecompressor_stream:
    def test_decompress(self):

