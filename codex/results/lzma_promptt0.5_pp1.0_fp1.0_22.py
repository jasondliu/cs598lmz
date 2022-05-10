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
d.decompress(b'x')
assert d.unused_data == b'x'
assert d.decompress(b'y') == b''
assert d.unused_data == b'xy'
assert d.decompress(b'z') == b''
assert d.unused_data == b'xyz'

# Test that unused_data is reset when calling flush()
d = lzma.LZMADecompressor
