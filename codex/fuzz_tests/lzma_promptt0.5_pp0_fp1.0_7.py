import lzma
# Test LZMADecompressor

data = b"".join(chr(i % 256) for i in range(10000))

# Compress using the lzma module
compressed = lzma.compress(data)

# Decompress using the LZMADecompressor class
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Check that the decompressed data is the same as the original data
assert data == decompressed

# Check that the LZMADecompressor class has decompressed the
# entire stream
assert decompressor.unused_data == b""

# Check that the LZMADecompressor class has finished decompression
assert decompressor.eof is True
# Test LZMADecompressor.decompress() with max_length

data = b"".join(chr(i % 256) for i in range(10000))

# Compress using the lzma module
compressed = lzma.compress(data)

# Decompress using the LZMAD
