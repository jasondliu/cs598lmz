import bz2
# Test BZ2Decompressor
bz_decompressor = bz2.BZ2Decompressor()
result = bz_decompressor.decompress(compressed_data)
result == original_data

# Test BZ2File
with bz2.BZ2File('bz2_compressed.bz2', 'wb') as f:
    f.write(original_data)
with bz2.BZ2File('bz2_compressed.bz2', 'rb') as f:
    print(f.read(100))
    print(f.read(100))

# Compress data iteratively with BZ2Compressor
compressor = bz2.BZ2Compressor()
print(compressor.compress(b'x' * 10))
print(compressor.compress(b'x' * 10))
print(compressor.flush())

# Decompress data iteratively with BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(compressed_data))
print
