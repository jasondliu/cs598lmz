import bz2
# Test BZ2Decompressor.

# Test `r'
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh91AY&SY\xff') == b'hello'
assert d.unused_data == b'\xff'
# Test `w'
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh91AY&SYA\xff') == b'hello'
assert d.unused_data == b'\xff'
# Test `f'
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh91AY&SYF\xff') == b'hello'
assert d.unused_data == b'\xff'
# Test `\n'
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh91AY&SYE\xff') == b'hello\n'
assert d.unused_data == b'\xff'
# Test synthetic BZIP2_HDR_
