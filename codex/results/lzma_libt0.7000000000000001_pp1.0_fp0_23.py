import lzma
lzma.compress(b"Hello, world!")

import bz2
bz2.compress(b"Hello, world!")

import zlib
zlib.compress(b"Hello, world!")

import gzip
gzip.compress(b"Hello, world!")
# gzip.open() will open a compressed file and return a file-like object
import gzip

with gzip.open('/tmp/example.txt.gz', 'rt') as f:
    text = f.read()
    print(text)

# gzip.compress() will compress the data
import gzip

uncompressed_data = b'The same line, over and over.\n' * 10
compressed_data = gzip.compress(uncompressed_data)
len(uncompressed_data)
len(compressed_data)

# gzip.decompress() will decompress the data
import gzip

uncompressed_data = b'The same line, over and over.\n' * 10
compressed_data = g
