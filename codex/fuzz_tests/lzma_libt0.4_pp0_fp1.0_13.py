import lzma
lzma.decompress(open('data/lzma-compressed', 'rb').read())

# decompress gzip
import gzip
gzip.decompress(open('data/gzip-compressed', 'rb').read())

# decompress bzip2
import bz2
bz2.decompress(open('data/bzip2-compressed', 'rb').read())

# decompress zlib
import zlib
zlib.decompress(open('data/zlib-compressed', 'rb').read())

# decompress brotli
import brotli
brotli.decompress(open('data/brotli-compressed', 'rb').read())

# decompress xz
import lzma
lzma.decompress(open('data/xz-compressed', 'rb').read())

# decompress lz4
import lz4
lz4.block.decompress(open('data/lz4-compressed', 'rb').read())

# decompress snappy
import snappy
sn
