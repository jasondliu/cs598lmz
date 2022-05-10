import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
data = b"Hello world!"
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMADecompressor.decompress() with multiple calls

compressor = lzma.LZMACompressor()
data = b"Hello world!"
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed[:5])
decompressed += decompressor.decompress(compressed[5:])

print(decompressed)

# Test LZMADecompressor.decompress() with multiple calls
# and a max_length argument

compressor = lzma.LZMACompressor()
data = b"Hello world!"
