from lzma import LZMADecompressor
LZMADecompressor().decompress(b'...')

# But it is not a drop-in replacement for the gzip or zlib modules.
# For example, it does not provide a stream interface, and it can only decompress one chunk of data at a time.

# The lzma module also provides some low-level functionality:

# The LZMACompressor and LZMADecompressor classes can be used to compress and decompress data incrementally.
# The compress() and decompress() functions provide a convenient wrapper for one-shot compression and decompression.

# The LZMAFile class provides a convenient interface to LZMA compression and decompression,
# acting as a drop-in replacement for the built-in open() function.

# The LZMAError exception is raised in case of errors.

# The LZMA_FORMAT_AUTO, LZMA_FORMAT_XZ, LZMA_FORMAT_ALONE,
# LZMA_FORMAT_RAW, LZMA_CHECK_NONE, LZMA_CHECK_CRC32, LZMA_CHECK_CRC64,
