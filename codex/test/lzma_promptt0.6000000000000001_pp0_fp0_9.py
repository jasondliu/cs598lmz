import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
data = b"Hello world! " * 1000
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(data == decompressed)

# Test LZMADecompressor.stream
compressor = lzma.LZMACompressor()
data = b"Hello world! " * 1000
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = b""
