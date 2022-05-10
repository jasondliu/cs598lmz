import lzma
# Test LZMADecompressor with a bunch of data

class TestLZMADecompressor:
    def test_decompress_1(self):
        dc = lzma.LZMADecompressor()
        data = b"x" * 1000000
        cdata = lzma.compress(data)
        assert dc.decompress(cdata) == data
        assert dc.unused_data == b""
        assert dc.eof is True

    def test_decompress_2(self):
        dc = lzma.LZMADecompressor()
        data = b"x" * 1000000
        cdata = lzma.compress(data)
        assert dc.decompress(cdata[:500]) == b""
        assert dc.decompress(cdata[500:]) == data
        assert dc.unused_data == b""
        assert dc.eof is True

    def test_decompress_3(self):
        dc = lzma.LZMADecompressor()
        data = b"x" * 1000000
