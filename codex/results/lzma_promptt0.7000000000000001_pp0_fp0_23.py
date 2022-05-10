import lzma
# Test LZMADecompressor directly
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)
# Test with the incremental decompressor
decompressor = lzma.LZMADecompressor()
# The data is all in one chunk, so we just call decompress().
decompressor.decompress(data)
decompressor.flush()
# Test with a decompressor that has been initialized with preset
decompressor = lzma.LZMADecompressor(lzma.FORMAT_ALONE)
decompressor.decompress(data)
# Test incremental decompression
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)
decompressor.flush()
# Test incremental decompression with a decompressor that has been
# initialized with preset
decompressor = lzma.LZMADecompressor(lzma.FORMAT_ALONE)
decompressor.decompress(data)
decompressor.flush()
# Test with LZMADecompressor.
