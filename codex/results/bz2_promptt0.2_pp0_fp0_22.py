import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World')
print(data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

print(decompressor.decompress(data[:-1]))
print(decompressor.decompress(data[:-4]))

print(decompressor.unused_data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data[:-1]))
print(decompressor.unused_data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data[:-4]))
print(decompressor.unused_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
print(compressor.compress(b'Hello World'))
print(compressor.flush())

compressor = bz2.BZ2Compressor()
print(
