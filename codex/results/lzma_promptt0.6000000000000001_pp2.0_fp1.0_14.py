import lzma
# Test LZMADecompressor.seekable()

def test_seekable(data):
    c = lzma.LZMADecompressor()
    assert not c.seekable()

    c = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
    assert not c.seekable()

    c = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
    assert not c.seekable()

    c = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
    assert not c.seekable()

    c = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
    assert not c.seekable()

    c = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
    c.decompress(data[:5])
    assert not c.seekable()

    c = lzma.LZMADecompressor(format=lz
