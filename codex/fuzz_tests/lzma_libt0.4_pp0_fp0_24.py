import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

import gzip
gzip_compress = gzip.compress
gzip_decompress = gzip.decompress

import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

# import brotli
# brotli_compress = brotli.compress
# brotli_decompress = brotli.decompress

# import zstd
# zstd_compress = zstd.compress
# zstd_decompress = zstd.decompress

import lz4.frame
lz4_compress = lz4.frame.compress
lz4_decompress = lz4.frame.decompress

from . import blosc

# from . import lz4framed
# lz4framed_compress = lz4framed.compress
# lz4framed_dec
