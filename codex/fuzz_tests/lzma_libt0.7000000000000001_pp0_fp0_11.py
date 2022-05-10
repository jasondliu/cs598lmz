import lzma
lzma.LZMADecompressor().decompress(data)

import bz2
bz2.BZ2Decompressor().decompress(data)

import zlib
zlib.decompress(data, -15)

import gzip
gzip.decompress(data)

import zstd
zstd.ZstdDecompressor().decompress(data)

import brotli
brotli.decompress(data)
</code>

