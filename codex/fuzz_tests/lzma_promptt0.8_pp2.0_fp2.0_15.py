import lzma
# Test LZMADecompressor
assert lzma.LZMADecompressor().decompress(b'') == b''
assert lzma.LZMADecompressor().decompress(b'\x00') == b''
assert lzma.LZMADecompressor().decompress(b'\x04\x22\x4d\x18\x64') == b'foo'
assert lzma.LZMADecompressor().decompress(b'\x01\x01\x00') == b'\x00' * (1 << 18)
assert lzma.LZMADecompressor().decompress(b'\x02\x01\xdf\xff\x20') == b'\x00' * (1 << 18)
assert lzma.LZMADecompressor().decompress(b'\x02\x01\xdf\xff\x40') == b'\x00' * (1 << 21)
assert lzma.LZMADecompressor().decompress(b'\x04\
