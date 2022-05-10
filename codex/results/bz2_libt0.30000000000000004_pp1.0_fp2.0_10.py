import bz2
bz2.decompress(data)

# The bz2 module includes a complete implementation of bzip2 compression.
# It is possible to compress and decompress using bz2 using only the
# functions in the module.

# The compress() function takes a string and returns a bytes object
# containing compressed data.

# The decompress() function takes a bytes object and returns a string
# containing the uncompressed data.

# The compress() and decompress() functions both take an optional parameter
# called compresslevel. This is an integer from 1 to 9 controlling the level
# of compression; the default is 9.

# The higher the compression level, the more time is spent compressing data.
# Higher compression levels also result in smaller compressed files.

# The bz2 module also includes a convenience function called open() that
# works like the open() function in the standard library but handles
# bzip2-compressed files automatically.

# The open() function takes a filename, a mode, and an optional compresslevel
# argument. It returns a file object that can be used like a regular file.

# The mode argument can be '
