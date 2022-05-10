import bz2
bz2.decompress(bz2.compress(b'Hello world'))

import lzma
lzma.decompress(lzma.compress(b'Hello world'))

import zlib
zlib.decompress(zlib.compress(b'Hello world'))

import brotli
brotli.decompress(brotli.compress(b'Hello world'))
