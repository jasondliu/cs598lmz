import bz2
bz2.decompress(bz2_data)

# The data returned by a BZ2File object's read() method
# is of type 'bytes' just as with regular files.
type(bz2_data)

# ----------------------------
# <<
# ----------------------------
# You can get a file-like interface to an in-memory compressed string using
# the BZ2Compressor and BZ2Decompressor objects.

compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

compressed_data = compressor.compress(b"this is some uncompressed data")
compressed_data += compressor.flush()

data = decompressor.decompress(compressed_data)
data += decompressor.flush()

# It's not possible to just decompress a compressed file right in memory.
# There are two reasons for that:
# 1. Not always possible.
# 2. It would require some kind of in-memory decompression buffer
#    that might not fit into memory and that would complicate the API.
