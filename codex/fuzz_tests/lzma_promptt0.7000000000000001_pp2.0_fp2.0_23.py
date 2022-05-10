import lzma
# Test LZMADecompressor

class TestDecompressor:
    def test_decompress(self):
        s = b"Hello World"
        d = lzma.LZMADecompressor()
        assert d.decompress(s) == s
        assert d.unused_data == b""
        assert d.eof is True

    def test_unused_data(self):
        s = b"Hello World"
        d = lzma.LZMADecompressor()
        assert d.decompress(b"FooBar") == b""
        assert d.unused_data == b"FooBar"
        assert d.eof is False
        assert d.decompress(s) == s
        assert d.unused_data == b""
        assert d.eof is True

    def test_incomplete(self):
        s = b"Hello World"
        d = lzma.LZMADecompressor()
        assert d.decompress(s[:6]) == s[:6]
        assert d.unused_data
