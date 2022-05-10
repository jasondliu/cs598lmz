import lzma
# Test LZMADecompressor.decompress() method.

def test_decompress():
    data = b"Hello world!"
    compressed = lzma.compress(data)
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(compressed) == data

# Test LZMADecompressor.decompress() method with multiple calls.

def test_decompress_multiple_calls():
    data = b"Hello world!"
    compressed = lzma.compress(data)
    decompressor = lzma.LZMADecompressor()

    chunksize = 4
    output = bytearray()
    for i in range(0, len(compressed), chunksize):
        output += decompressor.decompress(compressed[i:i+chunksize])
    assert output == data

# Test LZMADecompressor with extreme chunk sizes.

def test_extreme_chunksizes():
    data = b"Hello world!"
    compressed = lzma.compress(data)
    decomp
