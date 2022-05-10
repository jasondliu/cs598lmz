import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# So you have to use b'Hello World!' instead of 'Hello World!'.

# The compress() and decompress() functions both take an optional parameter, compresslevel,
# which is an integer from 1 to 9 controlling the level of compression; the default is 9.

# Higher compresslevel means more compression, but also slower compression and decompression.

# The bz2 module also includes a useful utility function called compress() that takes a string
# and returns the compressed version as a bytes object.

# The bz2 module also includes a useful utility function called decompress() that takes a bytes
# object and returns the decompressed version as a string.

# The bz2 module also includes a useful utility function called compress() that takes a string
# and returns the compressed version as a bytes object.

# The bz2 module also includes a useful utility function called decompress() that takes a bytes
# object and returns
