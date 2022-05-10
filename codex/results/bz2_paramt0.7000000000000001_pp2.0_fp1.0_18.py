from bz2 import BZ2Decompressor
BZ2Decompressor()

from lzma import LZMADecompressor
LZMADecompressor()

# from lzma import LZMAFile
# LZMAFile()

# from lzma import open as lzma_open
# lzma_open()

import zlib, gzip
zlib.decompressobj()
gzip.open('a.gz', 'rb')

# from zipfile import ZipFile
# zf = ZipFile('a.zip')
# zf.open('b.txt')

# from zlib import decompress, decompressobj
# decompress()
# decompressobj()
