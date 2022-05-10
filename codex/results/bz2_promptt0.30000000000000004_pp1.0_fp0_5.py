import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File('data/bzipped_file.bz2') as f:
    print(f.read())

# Compress data
with bz2.BZ2File('data/bzipped_file.bz2', 'wb') as f:
    f.write(data)

# Compress data with compress level
with bz2.BZ2File('data/bzipped_file.bz2', 'wb', compresslevel=9) as f:
    f.write(data)

# Compress data with compress level
with bz2.BZ2File('data/bzipped_file.bz2', 'wb', compresslevel=9) as f:
    f.write(data)

# Compress data with compress level
with bz2.BZ2File('data/bzipped_file.bz2', 'wb', compresslevel=9
