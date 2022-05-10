import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a simple string
    d = lzma.LZMADecompressor()
    data = b"Hello world!\n"
    compressed = d.compress(data)
    compressed += d.flush()
    assert d.decompress(compressed) == data

    # Test decompression with multiple calls to decompress()
    d = lzma.LZMADecompressor()
    data = b"Hello world!\n"
    compressed = d.compress(data)
    compressed += d.flush()
    assert d.decompress(compressed[:1]) == b""
    assert d.decompress(compressed[1:]) == data

    # Test decompression with multiple calls to decompress()
    # using only flush()
    d = lzma.LZMADecompressor()
    data = b"Hello world!\n"
    compressed = d.compress(data)
    compressed += d.flush()
    assert d.decompress(b
