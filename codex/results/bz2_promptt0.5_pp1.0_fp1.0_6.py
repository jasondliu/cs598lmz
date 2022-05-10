import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello world')
print(data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

print(decompressor.decompress(data))
print(decompressor.decompress(b'hello'))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

print(decompressor.decompress(b'hello'))
print(decompressor.decompress(b'world'))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
print(compressor.compress(b'hello'))
print(compressor.compress(b'world'))
print(compressor.flush())

compressor = bz2.BZ2Compressor()
print(compressor.compress(b'hello'))
print(compressor.flush())
print(compressor.compress(b'world'))

