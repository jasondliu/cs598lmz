import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a single-byte string
    compressor = lzma.LZMACompressor()
    data = b"\x00" * 1024
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(compressed) == data

    # Test decompression of a string larger than the internal buffer
    data = b"\x00" * 1024 * 1024
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    assert decompressor.decompress(compressed) == data

    # Test decompression of a string smaller than the internal buffer
    data = b"\x00" * 1024
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    assert decompressor.decompress(compressed) == data

    # Test decompression of a string which is exactly the size of the
    # internal buffer
