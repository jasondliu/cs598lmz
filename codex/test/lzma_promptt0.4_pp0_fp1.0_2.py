import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
data = b"This is a test"
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
