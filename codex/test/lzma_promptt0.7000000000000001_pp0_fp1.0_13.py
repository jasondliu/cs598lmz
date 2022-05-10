import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()
data = b'\x00\x00\x00\x00\x00\x00\x00\x00W\x13\x00\x00\x00\x00\x00\x00\x00'
decompressor.decompress(data)
