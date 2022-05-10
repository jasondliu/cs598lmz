import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename).read()

# zip
import zipfile
zipfile.ZipFile(filename).read()

# tar
import tarfile
tarfile.TarFile(filename).read()

# rar
import rarfile
rarfile.RarFile(filename).read()

# 7z
import py7zlib
py7zlib.Archive7z(filename).read()

# lzma
import lzma
lzma.LZMAFile(filename).read()

# xz
import lzma
lzma.LZMAFile(filename).read()

# bzip2
import bz2
bz2.BZ2File(filename).read()

# lz4
import lz4
lz4.LZ4File(filename).read()

# lz4hc
import lz4
lz4.LZ4File(filename).read()

# brotli
import brotli
brot
