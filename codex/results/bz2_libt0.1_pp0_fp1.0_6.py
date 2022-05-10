import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# The easiest way to do this in Python 3 is with the bytes() function, which takes a string of text and returns a bytes object.

# The bz2 module includes a command-line tool for compressing and decompressing files.
# To compress a file, run bzip2 with the name of the file to compress as an argument.
# The compressed file will have the same name as the original file, but with .bz2 appended to it.
# To decompress a file, run bzip2 with the -d option and the name of the compressed file as an argument.
# The decompressed file will have the same name as the compressed file, but without the .bz2 extension.

# The bz2 module is not as fast as the zlib module, but it has a much higher compression ratio.
# The bz2 module is a good choice for compressing data that will be stored for a long time,

