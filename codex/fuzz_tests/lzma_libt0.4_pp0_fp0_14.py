import lzma
lzma.decompress(open("../data/test.lzma", "rb").read())

# bz2
import bz2
bz2.decompress(open("../data/test.bz2", "rb").read())

# gzip
import gzip
gzip.decompress(open("../data/test.gz", "rb").read())

# zlib
import zlib
zlib.decompress(open("../data/test.zlib", "rb").read())

# snappy
import snappy
snappy.decompress(open("../data/test.snappy", "rb").read())

# brotli
import brotli
brotli.decompress(open("../data/test.br", "rb").read())

# zstandard
import zstandard
zstandard.ZstdDecompressor().decompress(open("../data/test.zst", "rb").read())

# lz4
import lz4.frame
lz4.frame.decompress(open("../data/test
