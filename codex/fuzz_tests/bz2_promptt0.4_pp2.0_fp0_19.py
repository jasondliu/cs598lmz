import bz2
# Test BZ2Decompressor.decompress()

bz2_decompressor = bz2.BZ2Decompressor()

with open('compressed.bz2', 'rb') as f:
    data = f.read(100)
    uncompressed_data = bz2_decompressor.decompress(data)
    print(uncompressed_data.decode('utf-8'))

print(bz2_decompressor.unused_data)

with open('compressed.bz2', 'rb') as f:
    data = f.read(100)
    uncompressed_data = bz2_decompressor.decompress(data)
    print(uncompressed_data.decode('utf-8'))

print(bz2_decompressor.unused_data)

with open('compressed.bz2', 'rb') as f:
    data = f.read(100)
    uncompressed_data = bz2_decompressor.decompress(data)
    print(uncompressed_data.decode('
