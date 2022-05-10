from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

import zlib
decompressor = zlib.decompressobj()
decompressor.decompress(data)

decompressor = zlib.decompressobj(-zlib.MAX_WBITS)
decompressor.decompress(data)

import bz2
bz2.decompress(data)

from gzip import GzipFile
with GzipFile(fileobj=io.BytesIO(data)) as gz_file:
    gz_file.read()

from gzip import decompress, compress
decompress(compress(b'ABC'))

import lzma
lzma.decompress(lzma.compress(b'ABC'))

import zlib
zlib.decompress(zlib.compress(b'ABC'))

import bz2
bz2.decompress(bz2.compress(b'ABC'))

from gzip import decompress, compress
decompress(compress(b'ABC'))

from gzip
