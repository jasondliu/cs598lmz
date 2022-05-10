import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World!')
print(data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

decompressor.decompress(data[:4])
print(decompressor.unused_data)

decompressor.decompress(data[4:])
print(decompressor.unused_data)

decompressor.decompress(b'BZh91AY&SY')
print(decompressor.unused_data)

decompressor.decompress(b'BZh91AY&SY')
print(decompressor.unused_data)

decompressor.decompress(b'BZh91AY&SY')
print(decompressor.unused_data)

decompressor.decompress(b'BZh91AY&SY')
print(decompressor.unused_data)

decompressor.decompress(b'BZh91AY&SY')
print
