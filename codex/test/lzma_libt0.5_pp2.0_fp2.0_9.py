import lzma
lzma.LZMADecompressor()

import bz2
bz2.BZ2Decompressor()

import zipfile
zipfile.ZIP_DEFLATED

import zlib
zlib.compressobj(level=9)

import lzma
lzma.LZMACompressor()

import bz2
bz2.BZ2Compressor()

import zlib
zlib.decompressobj()

import lzma
lzma.LZMADecompressor()

import bz2
bz2.BZ2Decompressor()

import zipfile
zipfile.ZIP_DEFLATED

import zlib
import time

compressor = zlib.compressobj(level=9)

with open('/tmp/zlib-compress.txt', 'wb') as f:
    for i in range(100):
        f.write(compressor.compress(bytes(i)))
        time.sleep(0.1)
    f.write(compressor.flush())

