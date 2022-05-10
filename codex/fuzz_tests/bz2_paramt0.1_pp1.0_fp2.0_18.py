from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.open()
# bz2.open() is a convenience function for opening bzip2-compressed files.
# It accepts the same arguments as the built-in open() function, but the file is decompressed on the fly.
# For example, to read a bzip2-compressed file:

with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# To write a bzip2-compressed file:

with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

# The mode argument can be any of 'r', 'rb', 'w', 'wb', 'a', or 'ab'.
# The default is 'rb'.

# The compresslevel argument is an integer from 1 to 9 controlling the level of compression;
# the default is 9.

# The file argument can be any object with a write() or read() method,
# like for example a file object opened for
