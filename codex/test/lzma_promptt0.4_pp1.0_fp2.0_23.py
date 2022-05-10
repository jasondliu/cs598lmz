import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"foo")
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
