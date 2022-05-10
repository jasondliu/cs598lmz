import lzma
lzma.decompress(open('data/compressed.lzma', 'rb').read())

import bz2
bz2.decompress(open('data/compressed.bz2', 'rb').read())

import gzip
gzip.decompress(open('data/compressed.gz', 'rb').read())

import zlib
zlib.decompress(open('data/compressed.zlib', 'rb').read())

import zstd
zstd.decompress(open('data/compressed.zstd', 'rb').read())

import brotli
brotli.decompress(open('data/compressed.br', 'rb').read())

import snappy
snappy.uncompress(open('data/compressed.sz', 'rb').read())

import lz4.frame
lz4.frame.decompress(open('data/compressed.lz4', 'rb').read())

import zstd
zstd.ZstdDecompressor().decompress(open('data/compressed.z
