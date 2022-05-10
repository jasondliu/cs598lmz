import lzma
# Test LZMADecompressor with some known data.
lzd = lzma.LZMADecompressor()
assert lzd.decompress(bytes([0x5d, 0x00, 0x00, 0x80, 0x00, 0xff])) == b'a'
# Test LZMADecompressor with some known data.
lzd = lzma.LZMADecompressor()
assert lzd.decompress(bytes([0x5d, 0x00, 0x00, 0x80, 0x00, 0xfe])) == b'a'
# Test LZMADecompressor with some known data.
lzd = lzma.LZMADecompressor()
assert lzd.decompress(bytes([0x5d, 0x00, 0x00, 0x80, 0x00, 0xfd])) == b'a'
# Test LZMADecompressor with some known data.
lzd = lzma.LZMADecompressor()
assert lzd.decompress(
