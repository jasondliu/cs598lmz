import lzma
lzma.LZMADecompressor()

import bz2
bz2.BZ2Decompressor()

import zlib
zlib.decompressobj()

import gzip
gzip.GzipFile('', 'r')

import zipfile
zipfile.ZipFile('', 'r')

import tarfile
tarfile.TarFile('', 'r')
