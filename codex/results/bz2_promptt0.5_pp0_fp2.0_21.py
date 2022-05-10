import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Decompress with bz2
bz2.decompress(compressed_data)

# Decompress with bz2file
with bz2.BZ2File('data/file.bz2', 'rb') as f:
    file_content = f.read()

# Compress with bz2
bz2.compress(file_content)

# Compress with bz2file
with bz2.BZ2File('data/file.bz2', 'wb') as f:
    f.write(file_content)
