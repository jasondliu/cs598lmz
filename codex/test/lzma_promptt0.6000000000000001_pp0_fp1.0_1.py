import lzma
# Test LZMADecompressor
lzc = lzma.LZMACompressor()
lzc.compress(b"hello")
lzc.compress(b" ")
lzc.compress(b"world!")
lzc.flush()

lzd = lzma.LZMADecompressor()
# Feed the entire compressed data to the decompressor object.
