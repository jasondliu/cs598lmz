import lzma
# Test LZMADecompressor.
d = lzma.LZMADecompressor()
d.decompress(b"")
