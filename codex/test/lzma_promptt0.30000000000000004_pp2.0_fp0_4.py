import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    compressor = lzma.LZMACompressor()
    data = b"a" * 1000000
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    assert len(compressed) < len(data)
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(compressed) == data
    assert decompressor.unused_data == b""
    assert decompressor.eof == True

def test_lzma_decompressor_unused_data():
    compressor = lzma.LZMACompressor()
    data = b"a" * 1000000
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    assert len(compressed) < len(data)
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(compressed[:-10]) == data[:-10]
    assert decompressor.unused_data == compressed[-10:]

