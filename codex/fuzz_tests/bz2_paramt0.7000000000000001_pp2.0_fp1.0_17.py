from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#gzip
from gzip import decompress
decompress(data)

#zlib
from zlib import decompress
decompress(data)

#lzma
import lzma
lzma.decompress(data)

#lz4
import lz4.block
lz4.block.decompress(data)

#lz4_legacy
import lz4.block
lz4.block.decompress(data, cname='LZ4_uncompress_unknownOutputSize')

#lzf
import lzf
lzf.decompress(data)

#lzma
import lzma
lzma.decompress(data)

#snappy
import snappy
snappy.decompress(data)

#zstd
import zstd
zstd.ZstdDecompressor().decompress(data)

#brotli
import brotli
brotli.decompress(data)

#delta
import delta

