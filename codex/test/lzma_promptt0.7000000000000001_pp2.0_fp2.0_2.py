import lzma
# Test LZMADecompressor by decompressing the data from its own compressed
# output.
compressor = lzma.LZMACompressor()
data = b'The quick brown fox jumps over the lazy dog'
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
