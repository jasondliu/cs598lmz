import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ,
                                 check=lzma.CHECK_NONE,
                                 preset=9)
compressor.compress(b"Hello, world!")
compressor.compress(b" Goodbye, world!")
compressor.flush()
