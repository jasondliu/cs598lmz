import bz2
bz2.compress(file_contents)

# Decompressing a compressed file.
uncompressed_data = bz2.decompress(compressed_data)

# Using bz2.open() like a regular file object.
with bz2.open(original_file, 'wt') as original_file_fileobj:
    original_file_fileobj.write(original_file_contents)
with bz2.open(compressed_file, 'rt') as compressed_file_fileobj:
    contents = compressed_file_fileobj.read()

# Use gzip module.

# Writing compressed files.
import gzip
with gzip.open(compressed_file, 'wt') as compressed_file_fileobj:
    compressed_file_fileobj.write(original_file_contents)

# Reading compressed files.
with gzip.open(compressed_file, 'rt') as compressed_file_fileobj:
    contents = compressed_file_fileobj.read()

# Compressing and decompressing in memory
original_data = b'A lot
