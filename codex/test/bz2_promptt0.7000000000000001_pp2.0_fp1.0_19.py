import bz2
# Test BZ2Decompressor.flush()

class TestBZ2Decompressor:
    def test_flush(self):
        input = bz2.compress(b"abcdefghijklmnopqrstuvwxyz")
        d = bz2.BZ2Decompressor()
        data = d.decompress(input)
        assert data == b"abcdefghijklmnopqrstuvwxyz"
        assert not d.unused_data
        assert not d.eof
        data = d.decompress(b"")
        assert data == b""
        assert not d.unused_data
        assert not d.eof
        data = d.flush()
        assert data == b""
        assert not d.unused_data
        assert d.eof

# Test BZ2Decompressor.decompress() with the maximum sized input

class TestBZ2DecompressorLargeInput:
    def _test_decompress(self, input, expected):
        d = bz2.BZ2Decompressor()
