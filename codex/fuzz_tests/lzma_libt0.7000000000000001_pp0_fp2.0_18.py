import lzma
lzma.LZMADecompressor().decompress(lzma.LZMACompressor().compress(b'a' * 1000))

import bz2
bz2.BZ2Decompressor().decompress(bz2.BZ2Compressor().compress(b'a' * 1000))

import zlib
zlib.decompress(zlib.compress(b'a' * 1000))

import gzip
gzip.GzipFile(fileobj=gzip.open(io.BytesIO(gzip.compress(b'a' * 1000)))).read()

import zipfile
with zipfile.ZipFile(io.BytesIO(zipfile.ZIP_DEFLATED + zlib.compress(b'a' * 1000))) as file:
    file.read('a')

import tarfile
with tarfile.TarFile.open(
    mode='w:gz',
    fileobj=gzip.GzipFile(fileobj=io.BytesIO()),
) as file:
    file.add('a', fileobj
