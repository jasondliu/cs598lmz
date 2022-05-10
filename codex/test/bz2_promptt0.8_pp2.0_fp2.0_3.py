import bz2
# Test BZ2Decompressor class.

decomp = bz2.BZ2Decompressor()
assert decomp.unused_data == b''
data = decomp.decompress(b'BZh91AY&SY')
assert decomp.unused_data == b''
