import lzma
# Test LZMADecompressor.decompress()
data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
comp = lzma.LZMADecompressor()
assert comp.decompress(data) == data
# Test LZMADecompressor.decompress() with decompressor already used
comp = lzma.LZMADecompressor()
comp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
assert comp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') == data
# Test LZMADecompressor.decompress() with max_length
comp = lzma.LZMADecompressor()
assert comp.decompress(data, 1) == data[:1]
