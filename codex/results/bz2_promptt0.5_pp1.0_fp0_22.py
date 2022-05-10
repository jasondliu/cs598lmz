import bz2
# Test BZ2Decompressor.__init__

try:
    bz2.BZ2Decompressor()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.decompress()

d = bz2.BZ2Decompressor()

# Decompress a single chunk
print(d.decompress(b'BZh91AY&SY\x9e\x0b\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))

# Decompress multiple chunks
print(d.decompress(b'BZh91AY&SY\x9e\x0b\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08') + d.decompress(b'BZh91AY
