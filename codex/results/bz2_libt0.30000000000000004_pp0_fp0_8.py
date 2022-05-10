import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, which is not compatible with the
# text-based file object.

# To use bz2 with text-based file objects, wrap the file object with a
# BZ2File object.

with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(b'Hello World!')

with bz2.BZ2File('file.bz2', 'r') as f:
    print(f.read())

# BZ2File objects also support the context manager protocol, so you can
# use them in a with statement.

# The bz2 module also provides a command-line tool for compressing and
# decompressing files.

# The bz2.compress() and bz2.decompress() functions are also available
# in the bz2 module.

# The bz2 module is a good choice for compressing data for storage or
# transmission when the size of
