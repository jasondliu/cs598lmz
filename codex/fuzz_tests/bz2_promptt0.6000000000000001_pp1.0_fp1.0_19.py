import bz2
# Test BZ2Decompressor.read()
decomp = bz2.BZ2Decompressor()
data = decomp.decompress(bz2data)
print(data == bz2data)

# Test BZ2Decompressor.read() with a buffer size of 1
decomp = bz2.BZ2Decompressor()
d = decomp.decompress(bz2data[:1])
d += decomp.decompress(bz2data[1:])
print(d == bz2data)

# Test BZ2Decompressor.read() with a buffer size of 2
decomp = bz2.BZ2Decompressor()
d = decomp.decompress(bz2data[:2])
d += decomp.decompress(bz2data[2:])
print(d == bz2data)

# Test BZ2Decompressor.read() with a buffer size of 3
decomp = bz2.BZ2Decompressor()
d = decomp.decompress(bz2data[:3])
d += decomp.decomp
