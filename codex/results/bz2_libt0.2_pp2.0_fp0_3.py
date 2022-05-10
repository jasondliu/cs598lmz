import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import lz4.frame
lz4.frame.decompress(lz4.frame.compress(b'hello world'))

import brotli
brotli.decompress(brotli.compress(b'hello world'))

import snappy
snappy.decompress(snappy.compress(b'hello world'))

import zstandard
zstandard.ZstdDecompressor().decompress(zstandard.ZstdCompressor().compress(b'hello world'))

import zopfli.zlib
zopfli.zlib.decompress(zopfli.zlib.compress(b'hello world'))

import zopfli.gzip
zopfli.gzip.decomp
