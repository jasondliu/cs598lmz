import bz2
bz2.decompress(bz2_data)

# gzip
import gzip
gzip.decompress(gzip_data)

# lzma
import lzma
lzma.decompress(lzma_data)

# lz4
import lz4.block
lz4.block.decompress(lz4_data)

# zstd
import zstd
zstd.decompress(zstd_data)

# brotli
import brotli
brotli.decompress(brotli_data)
