from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

import bz2
bz2.decompress(compressed)

import zlib
zlib.decompress(compressed)

import brotli
brotli.decompress(compressed)

import lz4.frame
lz4.frame.decompress(compressed)

import lz4.block
lz4.block.decompress(compressed)

import snappy
snappy.uncompress(compressed)

import zstandard
zstandard.ZstdDecompressor().decompress(compressed)

import blosc
blosc.decompress(compressed)

import liblzf
liblzf.decompress(compressed)

import lzf
lzf.decompress(compressed)

import lzham_cffi
lzham_cffi.decompress(compressed)

import lzss
lzss.decompress(compressed)

import lzw_codec
lzw_codec
