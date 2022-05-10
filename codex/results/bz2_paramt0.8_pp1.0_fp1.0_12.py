from bz2 import BZ2Decompressor
BZ2Decompressor().decompress()

from gzip import GzipFile
GzipFile().read()

from zlib import decompress
decompress()

from zipfile import ZipFile
ZipFile().read()
