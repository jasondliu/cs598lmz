import lzma
lzma.decompress(open(fname, "rb").read())

# decompress lzma file
import lzma
lzma.decompress(open(fname, "rb").read())

# decompress xz file
import lzma
lzma.decompress(open(fname, "rb").read())

# decompress bzip2 file
import bz2
bz2.decompress(open(fname, "rb").read())

# decompress gzip file
import gzip
gzip.decompress(open(fname, "rb").read())

# decompress zlib file
import zlib
zlib.decompress(open(fname, "rb").read())

# decompress lz4 file
import lz4.block
lz4.block.decompress(open(fname, "rb").read())

# decompress snappy file
import snappy
snappy.decompress(open(fname, "rb").read())

# decompress lzf file
import lzf
