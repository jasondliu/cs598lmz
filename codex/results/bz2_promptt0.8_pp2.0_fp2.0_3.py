import bz2
# Test BZ2Decompressor class.

decomp = bz2.BZ2Decompressor()
assert decomp.unused_data == b''
data = decomp.decompress(b'BZh91AY&SY')
assert decomp.unused_data == b''
assert data == b"hello world"
print(len(data))
# Test BZ2Decompressor.decompress() with multiple decompress calls.

decomp = bz2.BZ2Decompressor()
assert decomp.unused_data == b''
data = decomp.decompress(b'BZh71')
assert decomp.unused_data == b'BZh71'
assert data == b''
data = decomp.decompress(b'AY&SY')
assert decomp.unused_data == b''
assert data == b"hello world"
# Test BZ2Decompressor.decompress() with multiple decompress calls and a
# max_length argument.

decomp = bz2.BZ2Decompressor()
assert decomp.unused_data == b''
data = decomp.dec
