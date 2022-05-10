import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.decompress
decomp = lzma.LZMADecompressor()
data = b'\x5d\x00\x00\xff\xff\x03\x00\x04\x00\x04\x00\x00\x00'
