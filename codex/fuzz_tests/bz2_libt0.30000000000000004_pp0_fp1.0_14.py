import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import zlib
zlib.decompress(zlib.compress(b'Hello World'))

import lzma
lzma.decompress(lzma.compress(b'Hello World'))

import lz4
lz4.decompress(lz4.compress(b'Hello World'))

import brotli
brotli.decompress(brotli.compress(b'Hello World'))

import snappy
snappy.decompress(snappy.compress(b'Hello World'))

import zstd
zstd.decompress(zstd.compress(b'Hello World'))

import xxhash
xxhash.xxh32(b'Hello World').hexdigest()

import xxhash
xxhash.xxh64(b'Hello World').hexdigest()

import xxhash
xxhash.xxh3_64(b'Hello World').hexdigest()

import xxhash
xxhash.xx
