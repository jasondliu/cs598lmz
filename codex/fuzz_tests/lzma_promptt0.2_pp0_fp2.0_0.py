import lzma
# Test LZMADecompressor

# Test decompression of empty data
d = lzma.LZMADecompressor()
assert d.decompress(b'') == b''

# Test decompression of empty data with max_length
d = lzma.LZMADecompressor()
assert d.decompress(b'', max_length=0) == b''

# Test decompression of empty data with max_length > 0
d = lzma.LZMADecompressor()
assert d.decompress(b'', max_length=1) == b''

# Test decompression of empty data with max_length < 0
d = lzma.LZMADecompressor()
assert d.decompress(b'', max_length=-1) == b''

# Test decompression of data with max_length < 0
d = lzma.LZMADecompressor()
assert d.decompress(b'\x00', max_length=-1) == b''

# Test decompression of data with max_length == 0
d = l
