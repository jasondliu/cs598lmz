import bz2
# Test BZ2Decompressor

# Test BZ2Decompressor.flush()

data = bz2.compress(b"this is a test")
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.decompress(b""))
print(decompressor.flush())
print(decompressor.decompress(b"and a final bit of data"))

# Test BZ2Decompressor.decompress()

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(b"BZh91AY&SY"))
print(decompressor.decompress(b"A"))
print(decompressor.decompress(b"A"))
print(decompressor.decompress(b"A"))
print(decompressor.decompress(b"A"))
print(decompressor.decompress(b"A"))
print(decompressor.decompress(b"A"))
print(decompressor.decompress
