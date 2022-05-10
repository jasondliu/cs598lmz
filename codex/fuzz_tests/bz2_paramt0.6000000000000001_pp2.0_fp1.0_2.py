from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"hello world"))

# bz2.compress() and bz2.decompress() provide a complete one-shot interface for
# compression and decompression.

# The compress() function returns a bytes object containing compressed data.
# The decompress() function returns a bytes object containing the uncompressed data.

# If you want to compress data sequentially in small chunks, you can use a BZ2Compressor
# object. It provides a compress() method, just like the bz2.compress()
# function. It also provides an eof attribute that is True when all of the data has been
# compressed.

# The BZ2Decompressor class provides a similar interface for decompressing data in
# chunks.

# These classes are used internally by the bz2 module, but they're also useful
# if you're doing your own processing of compressed data in chunks.

# For example, you could use BZ2Compressor to feed data to a socket or write it to a
# file. The following example feeds data to a BZ2Compressor in small chunks
