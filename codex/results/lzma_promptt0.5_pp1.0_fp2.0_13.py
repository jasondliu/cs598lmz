import lzma
# Test LZMADecompressor.eof

data = b"".join(b"test" * 100)

# Compress data
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()

# Decompress all data
decompressed = decompressor.decompress(compressed)
assert decompressor.eof is True

# Decompress partially
decompressed = decompressor.decompress(compressed[:len(compressed)//2])
assert decompressor.eof is False

# Decompress the rest of data
decompressed += decompressor.decompress(compressed[len(compressed)//2:])
assert decompressor.eof is True

# Decompress empty data
decompressed = decompressor.decompress(b"")
assert decompressor.eof is True

# Decompress more than needed
decompressed = decompressor.decompress(compressed + b"more")
assert decompressor.
