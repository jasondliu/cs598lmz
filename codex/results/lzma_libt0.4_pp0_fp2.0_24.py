import lzma
lzma.LZMADecompressor().decompress(open('data/compressed.xz', 'rb').read())

# bzip2
import bz2
bz2.BZ2Decompressor().decompress(open('data/compressed.bz2', 'rb').read())

# gzip
import gzip
gzip.GzipFile('data/compressed.gz').read()

# brotli
import brotli
brotli.decompress(open('data/compressed.br', 'rb').read())

# zstd
import zstd
zstd.ZstdDecompressor().decompress(open('data/compressed.zst', 'rb').read())

# lz4
import lz4.frame
lz4.frame.decompress(open('data/compressed.lz4', 'rb').read())

# zlib
import zlib
zlib.decompress(open('data/compressed.zlib', 'rb').read())

# zopfli
import zopfli
