import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.open(filename)

# rar
import rarfile
rarfile.RarFile(filename)

# 7z
import py7zlib
py7zlib.Archive7z(filename)

# zstandard
import zstandard
zstandard.ZstdDecompressor().decompress(filename)

# brotli
import brotli
brotli.decompress(filename)

# lz4
import lz4
lz4.frame.open(filename)

# lzham
import lzham
lzham.decompress(filename)

# lzf
import lzf
lzf.open(filename)

# lzma
import lzma
lzma.open(filename)


