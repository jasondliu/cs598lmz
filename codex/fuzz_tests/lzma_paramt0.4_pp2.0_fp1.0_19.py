from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

import bz2
bz2.BZ2Compressor(compresslevel=9)
bz2.BZ2Decompressor()

import zlib
zlib.compress(data, level=-1, wbits=15, bufsize=1024)
zlib.decompress(data, wbits=15, bufsize=1024)
zlib.crc32(data, value=0)
zlib.adler32(data, value=0)
zlib.compressobj(level=-1, method=DEFLATED, wbits=15, memLevel=8, strategy=Z_DEFAULT_STRATEGY, zdict=None)
zlib.decompressobj(wbits=15, zdict=None)

import gzip
gzip.compress(data, compresslevel=9)
gzip.decompress(data)
gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)
gzip.G
