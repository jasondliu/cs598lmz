import lzma
# Test LZMADecompressor .decompress() method
def test_decompress():
    def gen_data(src, length=None):
        if length is None:
            length = len(src)
        while length > 0:
            if length >= len(src):
                yield src
                length -= len(src)
            else:
                yield src[:length]
                length = 0

    raw_data = b"this is a test of the emergency broadcast system"
    cdata = lzma.compress(raw_data)
    assert lzma.decompress(cdata) == raw_data

    d = lzma.LZMADecompressor()
    assert d.decompress(cdata) == raw_data
    assert d.unused_data == b""
    assert d.eof is True

    d = lzma.LZMADecompressor()
    data = gen_data(cdata)
    assert d.decompress(next(data)) == b""
    assert d.decompress(next(data)) == raw_data
    assert d
