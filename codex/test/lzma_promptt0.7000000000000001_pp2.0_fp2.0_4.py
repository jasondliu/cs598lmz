import lzma
# Test LZMADecompressor with a small data.
compressor = lzma.LZMACompressor()
data = b'this is the original, uncompressed data'
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(compressed)
