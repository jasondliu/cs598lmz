import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()

compressor.compress(b"hello")
compressor.compress(b"world")
compressor.flush()

