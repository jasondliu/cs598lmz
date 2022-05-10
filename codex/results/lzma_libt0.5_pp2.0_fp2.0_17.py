import lzma
lzma.decompress(open('../data/example/example.lzma', 'rb').read())

import bz2
bz2.decompress(open('../data/example/example.bz2', 'rb').read())

import gzip
gzip.decompress(open('../data/example/example.gz', 'rb').read())

import zlib
zlib.decompress(open('../data/example/example.zlib', 'rb').read())

import brotli
brotli.decompress(open('../data/example/example.br', 'rb').read())

import snappy
snappy.decompress(open('../data/example/example.snappy', 'rb').read())

import lzf
lzf.decompress(open('../data/example/example.lzf', 'rb').read())

import lz4
lz4.decompress(open('../data/example/example.lz4', 'rb').read())

import lz4framed
lz4
