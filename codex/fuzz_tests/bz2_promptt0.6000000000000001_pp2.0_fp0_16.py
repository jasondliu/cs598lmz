import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Print the decompressed data
print(decompressed_data)

# bz2.open returns a file-like object
with bz2.open(compressed_file, 'rt') as f:
    print(f.read())

# Read the compressed file and decompress it
with bz2.open(compressed_file, 'rt') as f:
    file_content = f.read()
    print(file_content)

# https://docs.python.org/3/library/gzip.html
import gzip
# Open the compressed file
with gzip.open(compressed_file, 'rt') as f:
    file_content = f.read()
    print(file_content)

# Read the compressed file and decompress it
with gzip.open(compressed_file, 'rt') as f:
    file_content = f.read()
    print(file_content)

import gzip
# Create
