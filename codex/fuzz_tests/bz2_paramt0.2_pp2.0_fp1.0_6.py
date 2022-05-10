from bz2 import BZ2Decompressor
BZ2Decompressor()

from gzip import GzipFile
GzipFile()

from zlib import decompress
decompress(b'x\x9cK\xcb\xcf\x07\r\x00\x02\x82\x01E')

from lzma import LZMADecompressor
LZMADecompressor()

from lzma import open as lzma_open
lzma_open('/tmp/foo.xz', 'rb')

from zipfile import ZipFile
ZipFile('/tmp/foo.zip')

from tarfile import TarFile
TarFile('/tmp/foo.tar')

from tarfile import open as tar_open
tar_open('/tmp/foo.tar')

from tarfile import TarInfo
TarInfo('/tmp/foo.tar')

from tarfile import TarError
TarError()

from tarfile import ReadError
ReadError()

from tarfile import CompressionError
CompressionError()

from tarfile import StreamError
StreamError()

from tarfile import ExtractError
Ext
