import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import gzip
gzip.decompress(gzip.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import lz4
lz4.decompress(lz4.compress(b'hello world'))

import brotli
brotli.decompress(brotli.compress(b'hello world'))

import snappy
snappy.decompress(snappy.compress(b'hello world'))

import zstandard
zstandard.ZstdDecompressor().decompress(zstandard.ZstdCompressor().compress(b'hello world'))

import lzf
lzf.decompress(lzf.compress(b'hello world'))

import lzma
lzma.decompress
