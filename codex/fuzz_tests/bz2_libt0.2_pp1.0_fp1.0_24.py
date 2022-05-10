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

# lz4
import lz4.block
lz4.block.decompress(lz4_data)

# lz4framed
import lz4.frame
lz4.frame.decompress(lz4framed_data)

# snappy
import snappy
snappy.uncompress(snappy_data)

# zstandard
import zstandard
zstd_ctx = zstandard.ZstdDecompressor()
zstd_ctx.decompress(zstandard_data)

# blosc
import blosc
blosc.decompress(blosc_data)

