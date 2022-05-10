import bz2
bz2.decompress(bz2.compress(data))

# bz2.compress() returns a bytes object
# bz2.decompress() requires a bytes object
# bz2.compress() and bz2.decompress() both have an optional parameter: compresslevel
# The compresslevel argument is an integer from 1 to 9 controlling the level of compression; 1 is fastest and produces the least compression, and 9 is slowest and produces the most compression. The default is 9.

# bz2.BZ2Compressor() and bz2.BZ2Decompressor()
# bz2.BZ2Compressor() and bz2.BZ2Decompressor() are the objects that perform the compression and decompression.
# bz2.BZ2Compressor.compress() and bz2.BZ2Decompressor.decompress() are the methods that do the actual work.
# bz2.BZ2Compressor.compress() returns a bytes object, and bz2.BZ2Decompressor.decompress() requires a bytes object.
#
