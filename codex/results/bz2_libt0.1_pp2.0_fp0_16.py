import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# The easiest way to do this in Python 3 is to use the data argument to the open() function.

with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World!')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# The bz2 module includes a command-line tool for manipulating bzip2 files.
# The bzcat command is similar to the zcat command, but for bzip2 files.

# $ bzcat file.bz2
# Hello World!

# The bz2 module also includes a command-line tool for compressing and decompressing files.
# The bzip2 command is similar to the gzip command, but for bzip2 files.

# $ bzip2 file
# $ ls
# file.bz
