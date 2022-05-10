import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
data = b"Hello, world!"
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMADecompressor.decompress()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMADecompressor.decompress() with multiple calls

decompressor = lzma.LZMADecompressor()

decompressed = decompressor.decompress(compressed[:4])
decompressed += decompressor.decompress(compressed[4:])

print(decompressed)

# Test LZMADecompressor.decompress() with multiple calls and a buffer

decompressor = lzma.L
