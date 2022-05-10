import bz2
# Test BZ2Decompressor

data = bz2.compress(b"this is a test")
print(data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.decompress(data))
print(decompressor.decompress(b"BZh91AY&SY"))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(b"BZh91AY&SY"))
print(decompressor.decompress(b"BZh91AY&SY"))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(b"BZh91AY&SY"))
print(decompressor.decompress(b"BZh91AY&SY"))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(b"BZh91AY&SY"))
print(decompressor.decompress(b"
