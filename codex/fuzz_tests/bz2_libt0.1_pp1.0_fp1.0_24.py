import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# The easiest way to get these is with the bytes() and bytearray() types introduced in Python 3.

# The bz2 module includes a command-line tool for compression and decompression called bzip2.
# It is a good idea to use this tool for compressing files that will be used with older Python versions,
# which do not include the bz2 module.

# The bz2 module is not capable of directly handling tar archives.
# However, the tarfile module can handle tar archives that have been compressed using the bz2 compression algorithm.

# The bz2 module is also not capable of handling ZIP files.
# However, the zipfile module can handle ZIP files that have been compressed using the bz2 compression algorithm.

# The bz2 module is not capable of handling gzip files.
# However, the gzip module can handle gzip files that have been compressed using the bz2
