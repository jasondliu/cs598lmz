import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

try:
    import zstd
    zstd_compress = zstd.compress
    zstd_decompress = zstd.decompress
except ImportError:
    zstd_compress = None
    zstd_decompress = None

#
# The following code provides an implementation of the LZ4
# compression format. It is based on the code from the lz4
# module, but modified to conform to the LZ4 frame format
# specification version 1.5.1.
#

def _lz4_decompress(source, uncompressed_size,
                    max_block_size=LZ4_MAX_BLOCK_SIZE):
    """Decompress LZ4 data from a buffer."""
    max_block_size = min(max_block_size, LZ4_MAX_BLOCK_SIZE)
    max_block_size = max(max_block_size, LZ4_MIN_BLOCK_SIZE)

