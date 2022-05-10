import lzma
# Test LZMADecompressor().decompress()
compressed = lzma.compress(b"Test")
compressor = lzma.LZMADecompressor()
compressor.decompress(compressed)
compressor.unused_data
compressor.eof
