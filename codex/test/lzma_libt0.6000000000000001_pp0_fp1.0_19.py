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

