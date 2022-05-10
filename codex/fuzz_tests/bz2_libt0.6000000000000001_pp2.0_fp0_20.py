import bz2
bz2.decompress(compressed)

# Compress a string
compressed = bz2.compress(uncompressed)
len(uncompressed)
len(compressed)

# Read the whole file as a single byte string
with gzip.open('example.txt.gz', 'rb') as input:
    print(input.read())

# Write chunks of data to a file
import gzip
with gzip.open('example.txt.gz', 'wb') as output:
    output.write(b'Contents of the example file go here.\n')

# Write with compression
import gzip
with gzip.open('example.txt.gz', 'wt') as output:
    output.write('Contents of the example file go here.\n')

# Read a compressed file
import gzip
with gzip.open('example.txt.gz', 'rt') as input:
    print(input.read())

# Read a chunk at a time
import gzip
with gzip.open('example.txt.gz', 'rt') as input:
    print(input
