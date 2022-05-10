import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

try:
    from zlib import compress as zlib_compress
    from zlib import decompress as zlib_decompress
except ImportError:
    zlib_compress = None
    zlib_decompress = None

#: The maximum size of a block of data to compress at once.
#:
#: This is used to limit the memory usage of the compression code.
#:
#: The default value is 32MB.
MAX_COMPRESSION_BLOCK_SIZE = 32 * 1024 * 1024

#: The maximum size of a block of data to decompress at once.
#:
#: This is used to limit the memory usage of the decompression code.
#:
#: The default value is 32MB.
MAX_DECOMPRESSION_BLOCK_SIZE = 32 * 1024 * 1024

#: The maximum size of a block of data to compress at once.
#:
#: This is used to limit the memory usage of the compression code.
#
