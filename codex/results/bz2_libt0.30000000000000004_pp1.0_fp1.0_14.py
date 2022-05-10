import bz2
bz2.decompress(bz2.compress(data))

# bz2.compress() returns a bytes object
# bz2.decompress() expects a bytes object

# If you need to compress a huge amount of data, you can use the compress() method in a loop. 
# Each call to compress() returns more compressed data. 
# The empty bytes object is returned when all of the data has been compressed.

# The compress() method takes one argument, the data to compress, and returns the compressed data. 
# The data must be a bytes object.

# The decompress() method takes one argument, the compressed data, and returns the decompressed data. 
# The data must be a bytes object.

# The decompress() method can be used in a loop if you need to decompress a huge amount of data. 
# Each call to decompress() returns more decompressed data. 
# The empty bytes object is returned when all of the data has been decompressed.

# The compress() and decompress() methods can also be used as context managers. 
# This allows you to use them with the
