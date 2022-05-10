import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

import gzip
gzip_compress = gzip.compress
gzip_decompress = gzip.decompress

import zlib
zlib_compress = zlib.compress
zlib_decompress = zlib.decompress

import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

import lz4.frame
lz4_compress = lz4.frame.compress
lz4_decompress = lz4.frame.decompress

import snappy
snappy_compress = snappy.compress
snappy_decompress = snappy.decompress

import blosc
blosc_compress = blosc.compress
blosc_decompress = blosc.decompress

import brotli
brotli_compress = brotli.compress
brotli_decomp
