import bz2
bz2.BZ2File(filename)

# Compress a file
bz2.compress(string)

# Decompress a file
bz2.decompress(string)

# Compress a file and write it to disk
with bz2.BZ2File(filename, 'w') as f:
    f.write(string)

# Decompress a file and write it to disk
with bz2.BZ2File(filename, 'r') as f:
    f.write(string)

# Compress a file and return the compressed data
bz2.compress(string)

# Decompress a file and return the decompressed data
bz2.decompress(string)

# Compress a file and return the compressed data
bz2.compress(string)

# Decompress a file and return the decompressed data
bz2.decompress(string)

# Compress a file and return the compressed data
bz2.compress(string)

# Decompress a file and return the decompressed data
b
