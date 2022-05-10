import bz2
bz2.decompress(bz2_compressed_data)

# gzip
import gzip
gzip.decompress(gzip_compressed_data)

# lzma
import lzma
lzma.decompress(lzma_compressed_data)

# zlib
import zlib
zlib.decompress(zlib_compressed_data)

# lzw
import lzw
lzw.decompress(lzw_compressed_data)

# lz4
import lz4
lz4.decompress(lz4_compressed_data)

# lz4hc
import lz4
lz4.decompress(lz4hc_compressed_data)

# snappy
import snappy
snappy.decompress(snappy_compressed_data)

# brotli
import brotli
brotli.decompress(brotli_compressed_data)

# zstd
import zstd
zstd.decompress(
