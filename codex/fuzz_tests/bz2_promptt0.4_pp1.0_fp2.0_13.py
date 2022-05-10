import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File('/tmp/file.bz2', 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File('/tmp/file.bz2', 'rb') as f:
    print(f.read())

# Compress and decompress with context manager
with bz2.BZ2File('/tmp/file.bz2', 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File('/tmp/file.bz2', 'rb') as f:
    print(f.read())

# Compress and decompress with context manager using compresslevel
with bz2.BZ2File('/tmp/file.bz2', 'wb', compresslevel=9) as f:
    f.write(compressed_data)

with bz2.
