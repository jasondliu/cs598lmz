import bz2
bz2.decompress(data)

# zlib
import zlib
zlib.decompress(data)

# lzma
import lzma
lzma.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# snappy
import snappy
snappy.decompress(data)

# lz4
import lz4
lz4.decompress(data)

# lz4framed
import lz4framed
lz4framed.decompress(data)

# lzma
import lzma
lzma.decompress(data)

# zstandard
import zstandard
zstandard.ZstdDecompressor().decompress(data)

# zopfli
import zopfli
zopfli.decompress(data)

# zopfli
import zopfli
zopfli.decompress(data)
