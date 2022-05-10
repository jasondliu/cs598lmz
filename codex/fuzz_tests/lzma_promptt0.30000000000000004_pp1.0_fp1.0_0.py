import lzma
# Test LZMADecompressor

# Create a compressor object
c = lzma.LZMADecompressor()

# Compress some data
data = b"Hello world! " * 1000
compressed = c.compress(data)

# Flush the compressor to get any remaining data
compressed += c.flush()

print("Compressed data:", len(compressed), "bytes")

# Create a decompressor object
d = lzma.LZMADecompressor()

# Decompress the data
decompressed = d.decompress(compressed)

print("Decompressed data:", len(decompressed), "bytes")

# Check that the decompressed data is the same as the original
assert decompressed == data

# Decompress the data with a convenience function
decompressed = lzma.decompress(compressed)

print("Decompressed data:", len(decompressed), "bytes")

# Check that the decompressed data is the same as the original
assert decompressed == data

# Decompress the data with a convenience function
decomp
