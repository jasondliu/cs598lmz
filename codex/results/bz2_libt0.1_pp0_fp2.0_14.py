import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() returns a bytes object

# bz2.decompress() requires a bytes-like object

# bz2.BZ2Compressor() and bz2.BZ2Decompressor() are also available

# bz2.BZ2Compressor() returns a compressor object that can be used to compress data incrementally

# bz2.BZ2Decompressor() returns a decompressor object that can be used to decompress data incrementally

# bz2.open() returns a file object that can be used to read or write compressed data

# bz2.open() accepts a filename, a mode, and an optional compression level

# bz2.open() defaults to compression level 9

# bz2.open() can be used as a context manager

# bz2.open() can be used to read and write compressed data

# bz2.open() can be used to read and write compressed data in text mode

# bz2.open() can
