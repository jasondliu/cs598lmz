import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress
lzma_decompress_error = lzma.LZMAError
lzma_decompress_error_msg = 'LZMA decompression failed'

# LZ4
try:
    import lz4
    lz4_compress = lz4.frame.compress
    lz4_decompress = lz4.frame.decompress
    lz4_decompress_error = lz4.LZ4FramedError
    lz4_decompress_error_msg = 'LZ4 decompression failed'
except ImportError:
    pass

# ZLIB
try:
    import zlib
    zlib_compress = zlib.compress
    zlib_decompress = zlib.decompress
    zlib_decompress_error = zlib.error
    zlib_decompress_error_msg = 'ZLIB decompression failed'
except ImportError:
    pass

