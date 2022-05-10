import lzma
# Test LZMADecompressor.closed with .flush()
compressor = lzma.LZMACompressor()
#compressor.flush(8 * 1024 * 1024)
compressor.flush(128 * 1024 * 1024)
print('compressor.closed=', compressor.closed)
#
# Test LZMADecompressor.closed with .finish()
compressor = lzma.LZMACompr
