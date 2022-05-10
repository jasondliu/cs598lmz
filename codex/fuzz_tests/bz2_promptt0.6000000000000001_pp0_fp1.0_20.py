import bz2
# Test BZ2Decompressor.

deco = bz2.BZ2Decompressor()
assert deco.decompress(b'BZh91AY&SY') == b'hello'
assert deco.unused_data == b''
assert deco.decompress(b'A') == b''
assert deco.unused_data == b'A'
assert deco.decompress(b'A') == b''
assert deco.unused_data == b'A'
assert deco.decompress(b'\x00\x01') == b'\x00\x01'
assert deco.unused_data == b''
assert deco.decompress(b'BZh91AY&SY') == b'hello'
assert deco.unused_data == b''

# Test BZ2Decompressor.decompress() with no unused data in the decompressor.
deco = bz2.BZ2Decompressor()
assert deco.decompress(b'BZh91AY&SY') == b'hello'
assert deco
