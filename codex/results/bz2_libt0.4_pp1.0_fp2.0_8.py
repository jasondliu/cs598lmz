import bz2
bz2.decompress(bz2.compress(data)) == data

# Compress data with bzip2 compression
data = b'Lots of data here'
with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

# Decompress data with bzip2 compression
with bz2.open('file.bz2', 'rt') as f:
    data = f.read()

# Compress data with bzip2 compression
data = b'Lots of data here'
with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(data)

# Decompress data with bzip2 compression
with bz2.BZ2File('file.bz2', 'r') as f:
    data = f.read()

# Compress data with bzip2 compression
data = b'Lots of data here'
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(data)

#
