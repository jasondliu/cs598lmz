import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# Decompress using context manager
with bz2.BZ2File('data.bz2', 'rb') as f:
    data = f.read()

# Compress using context manager
with bz2.BZ2File('data.bz2', 'wb') as f:
    f.write(data)

# Compress using context manager
with bz2.BZ2File('data.bz2', 'wb') as f:
    f.write(data)

# Compress using context manager
with bz2.BZ2File('data.bz2', 'wb') as f:
    f.write(data)

# Compress using context manager
with bz2.BZ2File('data.bz2', 'wb') as f:
    f.write(data)

# Compress using context manager
with bz2.BZ2File('data.bz2', 'wb') as f:

