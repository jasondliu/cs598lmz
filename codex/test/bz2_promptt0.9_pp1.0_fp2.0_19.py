import bz2
# Test BZ2Decompressor.
# Start with an empty buffer
d = bz2.BZ2Decompressor()
print(d.decompress(b'BZh91AY&SY'))
print(d.decompress(b'A'))
print(d.decompress(b'Y'))
# And uncompress the whole lot in one go
d = bz2.BZ2Decompressor()
