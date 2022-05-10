import lzma
# Test LZMADecompressor
assert lzma.LZMADecompressor().decompress(b'') == b''
assert lzma.LZMADecompressor().decompress(b'\x00') == b''
