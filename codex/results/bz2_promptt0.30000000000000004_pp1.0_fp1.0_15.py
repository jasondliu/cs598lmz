import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World')

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.decompress(data))

print(decompressor.unused_data)

print(decompressor.decompress(b'Hello World'))
print(decompressor.unused_data)

print(decompressor.decompress(b'Hello World'))
print(decompressor.unused_data)

print(decompressor.decompress(b'Hello World'))
print(decompressor.unused_data)

print(decompressor.decompress(b'Hello World'))
print(decompressor.unused_data)

print(decompressor.decompress(b'Hello World'))
print(decompressor.unused_data)

print(decompressor.decompress(b'Hello World'))
print(decompressor.unused_data)

print(
