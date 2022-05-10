import lzma
lzma.decompress(open('data.xz', 'rb').read())

# gzip
import gzip
gzip.decompress(open('data.gz', 'rb').read())

# bz2
import bz2
bz2.decompress(open('data.bz2', 'rb').read())

# zstd
import zstd
zstd.decompress(open('data.zst', 'rb').read())
