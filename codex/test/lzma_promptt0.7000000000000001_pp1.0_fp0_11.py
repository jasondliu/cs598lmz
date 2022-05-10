import lzma
# Test LZMADecompressor with a garbage file.
# It should raise EOFError on decompression.
d = lzma.LZMADecompressor()
