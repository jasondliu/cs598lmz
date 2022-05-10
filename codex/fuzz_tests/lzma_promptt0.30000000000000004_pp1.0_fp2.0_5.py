import lzma
# Test LZMADecompressor

# Create a compressor and decompressor
c = lzma.LZMACompressor()
d = lzma.LZMADecompressor()

# Compress some data
compressed = c.compress(b"Hello world!")
compressed += c.flush()

# Decompress the data
decompressed = d.decompress(compressed)

# Check that the decompressed data is the same as the original
assert decompressed == b"Hello world!"
# Test LZMADecompressor with a file

# Create a compressor and decompressor
c = lzma.LZMACompressor()
d = lzma.LZMADecompressor()

# Compress some data
with open("test.txt", "rb") as f:
    data = f.read()
    compressed = c.compress(data)
    compressed += c.flush()

# Decompress the data
decompressed = d.decompress(compressed)

# Check that the decompressed data is the same as the original
assert decompressed == data

