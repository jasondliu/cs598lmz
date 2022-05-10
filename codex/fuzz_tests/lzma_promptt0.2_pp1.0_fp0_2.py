import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test that the LZMADecompressor class can decompress
    # data after having been fed one byte at a time.
    data = b"foo" * 100000
    compressed = lzma.compress(data)
    decompressor = lzma.LZMADecompressor()
    result = b""
    for c in compressed:
        result += decompressor.decompress(bytes([c]))
    assert result == data

def test_lzma_decompressor_reset():
    # Test that the LZMADecompressor class can decompress
    # data after having been fed one byte at a time.
    data = b"foo" * 100000
    compressed = lzma.compress(data)
    decompressor = lzma.LZMADecompressor()
    result = b""
    for c in compressed:
        result += decompressor.decompress(bytes([c]))
    assert result == data
    decompressor.reset()
    result = b""

