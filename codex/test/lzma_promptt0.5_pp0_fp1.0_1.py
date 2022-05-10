import lzma
# Test LZMADecompressor and LZMACompressor classes

# Test LZMADecompressor and LZMACompressor classes

def test_lzma_compressor():
    c = lzma.LZMACompressor()
    data = b"foo"
    d = c.compress(data)
    d += c.flush()
    assert lzma.decompress(d) == data

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    data = b"foo"
    d = lzma.compress(data)
    assert c.decompress(d) == data
    assert c.unused_data == b""
    assert c.eof is True

def test_lzma_decompressor_unused_data():
    c = lzma.LZMADecompressor()
    data = b"foo"
    d = lzma.compress(data)
    assert c.decompress(d[:-1]) == b""
    assert c.unused
