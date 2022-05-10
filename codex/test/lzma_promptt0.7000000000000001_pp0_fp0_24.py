import lzma
# Test LZMADecompressor.decompress()
data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
comp = lzma.LZMADecompressor()
