import lzma
# Test LZMADecompressor

# Test empty input
d = lzma.LZMADecompressor()
assert d.decompress(b'') == b''
assert d.unused_data == b''

# Test multiple empty input
d = lzma.LZMADecompressor()
assert d.decompress(b'') == b''
assert d.unused_data == b''
assert d.decompress(b'') == b''
assert d.unused_data == b''

# Test that unused_data is reset when feeding new data
d = lzma.LZMADecompressor()
