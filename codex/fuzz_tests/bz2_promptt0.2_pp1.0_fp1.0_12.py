import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(decompressor.decompress(data))

print(decompressor.unused_data)

decompressor.decompress(decompressor.unused_data)

print(decompressor.unused_data)

decompressor.decompress(decompressor.unused_data)

print(decompressor.unused_data)

decompressor.decompress(decompressor.unused_data)

print(decompressor.unused_data)

decompressor.decompress(decompressor.unused_data)

print(decompressor.unused_data)

decompressor.decompress(decompressor.unused_data)

print(decompressor.unused_data)

decompressor.decompress(decompressor.unused_data)


