import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    decompressed_data = bz2_decompressor.decompress(f.read(100))

print(decompressed_data)
print(decompressed_data.decode('utf-8'))

# Test BZ2Compressor
bz2_compressor = bz2.BZ2Compressor()

compressed_data = bz2_compressor.compress(b'Hello, world!')
print(compressed_data)

compressed_data += bz2_compressor.flush()
print(compressed_data)

decompressed_data = bz2.decompress(compressed_data)
print(decompressed_data)

# BZ2File class
with bz2.BZ2File('data/compressed_file.bz2', 'wb') as output:
    for line in open('data/enwik8',
