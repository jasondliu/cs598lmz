import lzma
# Test LZMADecompressor

# Generate some random data
data = bytearray(os.urandom(100000))

# Compress it
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

# Decompress it
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Check that it works
assert decompressed == data

# Decompress using the convenience function
decompressed = lzma.decompress(compressed)
assert decompressed == data

# Decompress a file
with open('lzma-example.xz', 'rb') as input:
    with lzma.open(input) as decompressor:
        decompressed = decompressor.read()

# Check that it works
assert decompressed == data

# Decompress a file using the convenience function
with open('lzma-example.xz', 'rb') as input:
    decompressed = lzma.open(input).
