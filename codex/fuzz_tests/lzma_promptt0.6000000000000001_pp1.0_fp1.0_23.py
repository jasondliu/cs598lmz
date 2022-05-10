import lzma
# Test LZMADecompressor's ability to handle data longer than the read buffer
# size.
data = b'x' * (2 * lzma.LZMADecompressor.READ_SIZE + 1)
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data) + compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)
