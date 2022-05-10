import lzma
# Test LZMADecompressor

# Read the test file
with open("testdata/alice29.txt", "rb") as f:
    data = f.read()

# Compress it
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

# Decompress it
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Check that the decompression result matches the original data
assert decompressed == data

# Check that the unused_data attribute is empty
assert decompressor.unused_data == b""
# Test LZMADecompressor with multiple input chunks

# Read the test file
with open("testdata/alice29.txt", "rb") as f:
    data = f.read()

# Compress it
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

# Decompress it in chunks
decompressor =
