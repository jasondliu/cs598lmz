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
for chunk in compressed:
    decompressed += decompressor.decompress(chunk)
decompressed += decompressor.flush()
print(data == decompressed)

# Test LZMADecompressor.unused_data
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print
