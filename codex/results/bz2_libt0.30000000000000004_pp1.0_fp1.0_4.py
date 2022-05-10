import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# use bz2.compress() to compress a string, and bz2.decompress() to decompress it.

# The compress() function takes a string and returns a compressed version of the string. 
# The decompress() function takes a compressed string and returns the original uncompressed string.

# The compress() and decompress() functions work only on bytes-like objects. 
# If you need to compress or decompress strings, you have to encode and decode them first.

# The compress() function returns a bytes object, and the decompress() function requires a bytes object.

# The bz2 module does not support streaming compression. 
# You have to load the entire string into memory to compress or decompress it.

# The bz2 module does not support concatenation of compressed data.

# The bz2 module does not support random access to compressed data.

# The bz2 module does not support incremental compression.

# The bz2 module does not support incremental decompression.

# The bz2
