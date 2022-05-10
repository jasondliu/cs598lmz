import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"Some data")
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)
