import lzma
# Test LZMADecompressor.flush() and LZMACompressor.flush() with
# an empty input and an empty output.

def test_lzma_empty():
    c = lzma.LZMACompressor()
    d = lzma.LZMADecompressor()
    assert c.flush() == b''
    assert d.flush() == b''
    d.decompress(c.flush())
    d.decompress(c.flush())
    d.decompress(c.flush())
    assert d.flush() == b''
    d.decompress(b'123')
    assert d.flush() == b'123'
    assert d.flush() == b''
    d.decompress(b'x' * 200)
    assert d.flush() == b'x' * 200
    assert d.flush() == b''

# Test LZMADecompressor.decompress() with an empty input and an empty
# output.

def test_lzma_decompress_empty():
    d = lzma.LZM
