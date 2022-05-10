import lzma
# Test LZMADecompressor
assert lzma.LZMADecompressor().decompress(b'') == b''
