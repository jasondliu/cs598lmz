import lzma
# Test LZMADecompressor and LZMACompressor

def test_lzma_compress_decompress():
    c = lzma.LZMACompressor()
    d = lzma.LZMADecompressor()

    data = b'This is a test of the LZMA compression and decompression functions. ' * 100
    data += b'This is the end of the test data.'
    compressed = c.compress(data)
    compressed += c.flush()
    decompressed = d.decompress(compressed)

    assert decompressed == data

def test_lzma_compress_decompress_filter_none():
    c = lzma.LZMACompressor(filters=[])
    d = lzma.LZMADecompressor()

    data = b'This is a test of the LZMA compression and decompression functions. ' * 100
    data += b'This is the end of the test data.'
    compressed = c.compress(data)
    compressed += c.flush()
    decompressed = d.decompress(compressed
