import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
# Test decompression using 'read' method with large input
compressed = b'X' * (10 * 1024)
