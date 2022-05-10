import bz2
bz2.BZ2Compressor()

import zlib
zlib.compressobj()

import lzma
lzma.LZMACompressor()

import brotli
brotli.Compressor()

import lz4.frame
lz4.frame.compress()

import snappy
snappy.StreamCompressor()

import lz4.block
lz4.block.compress()

import zstd
zstd.ZstdCompressor()

import lzf
lzf.compress()

#
# Compression Decompressors
#

import gzip
gzip.GzipFile(mode='rb')

import bz2
bz2.BZ2Decompressor()

import zlib
zlib.decompressobj()

import lzma
lzma.LZMADecompressor()

import brotli
brotli.Decompressor()

import lz4.frame
lz4.frame.decompress()

import snappy
snappy.StreamDecomp
