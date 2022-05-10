import lzma
# Test LZMADecompressor

compressed = lzma.compress(b'This is a test')
compressed

compressor = lzma.LZMACompressor()
compressor.compress(b'This is a test')
compressor.flush()
