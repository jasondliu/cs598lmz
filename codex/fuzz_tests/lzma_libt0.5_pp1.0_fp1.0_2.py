import lzma
lzma.LZMADecompressor().decompress(open('./data/lzma_text.txt.xz', 'rb').read())

# bz2
import bz2
bz2.BZ2Decompressor().decompress(open('./data/bzip_text.txt.bz2', 'rb').read())

# zlib
import zlib
zlib.decompress(open('./data/zlib_text.txt.zlib', 'rb').read())

# gzip
import gzip
gzip.decompress(open('./data/gzip_text.txt.gz', 'rb').read())

# brotli
import brotli
brotli.decompress(open('./data/brotli_text.txt.br', 'rb').read())

# lz4
import lz4.frame
lz4.frame.decompress(open('./data/lz4_text.txt.lz4', 'rb').read())

# zstandard
import
