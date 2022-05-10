import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()

compressor.compress(b"hello")
compressor.compress(b"world")
compressor.flush()

compressed = compressor.compress(b"this is the end")
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()

decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()

print(decompressed)

# Test LZMADecompressor.decompress()

compressed = lzma.compress(b"hello world")
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMADecompressor.decompress() with multiple calls

compressed = lzma.compress(b"hello world")
decompressor = lzma.LZMADecompressor()
decompressed = b""


