import lzma
# Test LZMADecompressor.
# The decompressor has to be fed one byte at a time, to check it
# doesn't read more than that.  We do this by wrapping in a
# StringIO and calling read(1).
import io

testdata = b"".join([
    struct.pack("<5B6xLB5x", 0, 0, 0, 0, 0, lzma.FILTER_LZMA1, 0),
    lzma.compress(b"Hello world!")
    ])

def test_lzma_decompress(n):
    if io.StringIO is io.StringIO:
        raise ValueError("LZMADecompressor doesn't work with unicode strings")

    f = lzma.LZMADecompressor()
    with io.StringIO(testdata) as inbuf:
        assert f.read() == b""
        assert f.unused_data == b""
        assert f.eof == 0
        while 1:
            c = inbuf.read(n)
            if not c:
                break
            d =
