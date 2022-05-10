import lzma
# Test LZMADecompressor

# Test that the decompressor can be used in a streaming fashion
print("Testing LZMADecompressor")

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b"hello world" * 1000
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressed = decompressor.decompress(compressed)
assert decompressed == data

# Test that the decompressor can be used in a streaming fashion
print("Testing LZMADecompressor.decompress()")

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b"hello world" * 1000
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressed = b""
for i in range(0, len(compressed), 3):
    decompressed += decompressor.decompress(compressed[i:i+3])

assert decompressed == data
