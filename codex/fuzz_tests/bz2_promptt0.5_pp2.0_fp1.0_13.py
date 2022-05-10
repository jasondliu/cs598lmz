import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(compressed_data)
uncompressed_data

# Test BZ2File
with bz2.BZ2File('data.bz2', 'wb') as f:
    f.write(uncompressed_data)

with bz2.BZ2File('data.bz2', 'rb') as f:
    compressed_data = f.read()
compressed_data

# Compress data
compressed_data = bz2.compress(uncompressed_data)
compressed_data

# Decompress data
uncompressed_data = bz2.decompress(compressed_data)
uncompressed_data

# Compress and decompress in one step
uncompressed_data = bz2.decompress(bz2.compress(uncompressed_data))
uncompressed_data

# Compress using a context manager
with bz2.BZ2File('data.bz2
