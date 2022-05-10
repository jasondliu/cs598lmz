from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# The bz2 module also provides a convenient way to compress a file
# using bzip2 compression:
import bz2
bz2.BZ2File('bz2_compressed.bz2', 'wb').write(data)

# The bz2 module also provides a BZ2Compressor and BZ2Decompressor
# class to allow more control over the compression and decompression
# process. For example, you can use multiple compress() and decompress()
# calls to process a very large chunk of data without having to create
# an intermediate string to hold the entire data.

# The zlib module provides a lower-level interface to many of the
# compression and decompression algorithms used by zlib.
import zlib
compressed = zlib.compress(data)
decompressed = zlib.decompress(compressed)

# The zlib module also provides a set of convenience functions to
# compress and decompress files.
import zlib
with open('zlib_compressed.z', 'wb') as f:
    f.
