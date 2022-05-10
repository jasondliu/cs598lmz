from lzma import LZMADecompressor
LZMADecompressor().decompress(open('./archive.xz', 'rb').read())

# LZMA/XZ is a common compression used in python packages and linux
# distributions. But, since it requires the whole file to be decompressed
# at once, it's not recommended for larger files.

# The GzipFile class mimics most of the methods of the File class, but the data
# is compressed on the fly as its read and written.
from gzip import open as gzip_open
with gzip_open('somefile.gz', 'rt') as f:
    text = f.read()
with gzip_open('somefile.gz', 'wt') as f:
    f.write(text)

# The bz2 module includes support for compressing and decompressing using the
# bzip2 algorithm.
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

#
