import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

if hasattr(lzma, 'LZMADict'):
    # lzma >= 0.5.0
    def lzma_compress(data, *args):
        return lzma.LZMADict().compress(data)
    lzma_decompress = lzma.decompress
    lzma_method = lambda: lzma.LZMA_OK
else:
    lzma_method = lambda: lzma.CHECK_CRC32

_lzma_method = lzma_method

# --------------------------------------------------------------------
# Snappy

try:
    from snappy import compress as snappy_compress
    from snappy import decompress as snappy_decompress
except ImportError:
    _HAS_SNAPPY = False
else:
    _HAS_SNAPPY = True

# --------------------------------------------------------------------
# Bzip2

try:
    from bz2 import compress
