import lzma
# Test LZMADecompressor on a simple string.
compressor = lzma.LZMACompressor()
compressor.compress(b'begin ')
compressor.flush()
