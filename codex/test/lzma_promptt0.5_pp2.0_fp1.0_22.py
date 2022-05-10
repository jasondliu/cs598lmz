import lzma
# Test LZMADecompressor with an empty data stream.
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b"")
# Test LZMADecompressor with a truncated data stream.
decompressor = lzma.LZMADecompressor()
