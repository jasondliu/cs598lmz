import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

try:
    import lzma
    lzma_compress = lzma.compress
    lzma_decompress = lzma.decompress
except ImportError:
    lzma_compress = lzma_decompress = None

try:
    import zstd
    zstd_compress = zstd.compress
    zstd_decompress = zstd.decompress
except ImportError:
    zstd_compress = zstd_decompress = None

def get_compression_methods():
    methods = [
        ("none", None, None),
        ("zlib", zlib_compress, zlib_decompress),
        ("bz2", bz2_compress, bz2_decompress),
    ]
    if lzma_compress is not None:
        methods.append(("lzma", lzma_compress, lzma_decomp
