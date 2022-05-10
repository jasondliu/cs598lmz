import bz2
# Test BZ2Decompressor

# Test decompressor with a short string
d = bz2.BZ2Decompressor()
assert d.unused_data == b''
d.decompress(b'BZh91AY&SY')
assert d.unused_data == b''
assert d.decompress(b'A') == b'hello'
assert d.unused_data == b''

# Test decompressor with a long string
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh91AY&SY\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\
