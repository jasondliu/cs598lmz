import lzma
# Test LZMADecompressor

# Test decompress()
def test_decompress():
    # Test empty input
    d = lzma.LZMADecompressor()
    assert d.decompress(b"") == b""
    # Test decompress() with max_length
    data = b"\x00" * 100
    d = lzma.LZMADecompressor()
    assert d.decompress(data, max_length=50) == data[:50]
    assert d.decompress(b"", max_length=50) == b""
    # Test decompress() with max_length and unconsumed_tail
    d = lzma.LZMADecompressor()
    assert d.decompress(data, max_length=50) == data[:50]
    assert d.decompress(b"", max_length=50) == b""
    # Test decompress() with max_length and unconsumed_tail
    d = lzma.LZMADecompressor()
    assert d.decompress(data, max_
