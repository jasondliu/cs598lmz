import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# The easiest way to do this in Python 3 is to use the data argument to the open() function.

with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World!')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# The bz2 module includes a command-line tool for working with bzip2 files.
# It’s called bzcat and works just like zcat.

# The bz2 module is a good choice for compressing data that is going to be stored for a long time.
# It’s also a good choice for compressing data that is going to be sent over a network.
# It’s slower than gzip, but the compression ratio is better.

# The bz2 module is not as well supported as g
