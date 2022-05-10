import lzma
lzma_decompress = lzma.LZMADecompressor().decompress

# lz4
try:
    from lz4.block import decompress as lz4_decompress
except ImportError:
    lz4_decompress = None

# brotli
try:
    import brotli
    brotli_decompress = brotli.decompress
except ImportError:
    brotli_decompress = None

# zstd
try:
    import zstandard as zstd
    zstd_decompress = zstd.ZstdDecompressor().decompress
except ImportError:
    zstd_decompress = None

# blosc
try:
    import blosc
    blosc_decompress = blosc.decompress
except ImportError:
    blosc_decompress = None


# --- Compression types ---

