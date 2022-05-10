import bz2
bz2.compress(b'This is my data.')

# open, read, write
with bz2.open('file.bz2', 'wt') as f:
    f.write(b'This is my data.')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# bz2 compress and decompress
data = b'This is my data.'
compressed = bz2.compress(data)

bz2.decompress(compressed)

# bz2 compress level
data = b'This is my data.'
compressed = bz2.compress(data, compresslevel=9)

# zlib
import zlib
zlib.compress(b'This is my data.')
zlib.compress(b'This is my data.')[2:-4]

# quick compression
with open('file.gz', 'rt') as f:
    print(f.read())

with gzip.open('file.gz', 'wt') as f:
   
