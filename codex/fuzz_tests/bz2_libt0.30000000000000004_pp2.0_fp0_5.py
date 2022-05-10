import bz2
bz2.decompress(bz2_data)

# gzip
import gzip
gzip.decompress(gzip_data)

# lzma
import lzma
lzma.decompress(lzma_data)

# zlib
import zlib
zlib.decompress(zlib_data)

# brotli
import brotli
brotli.decompress(brotli_data)

# snappy
import snappy
snappy.decompress(snappy_data)

# lz4
import lz4
lz4.block.decompress(lz4_data)

# lz4hc
import lz4
lz4.frame.decompress(lz4hc_data)

# lz4framed
import lz4
lz4.frame.decompress(lz4framed_data)

# lz4framed_legacy
import lz4
lz4.frame.decompress(lz4framed_leg
