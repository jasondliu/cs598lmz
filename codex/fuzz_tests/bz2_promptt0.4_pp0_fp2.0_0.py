import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World')
print(data)

decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
    print(decompressor.decompress(data))
    print(decompressor.decompress(data))
except EOFError:
    pass

print(decompressor.unused_data)

decompressor = bz2.BZ2Decompressor()

for chunk in [data[:4], data[4:8], data[8:]]:
    print(decompressor.decompress(chunk))

print(decompressor.unused_data)

decompressor = bz2.BZ2Decompressor()

print(decompressor.decompress(data))
print(decompressor.unused_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

data = b'Hello World'

print(compressor.
