import bz2
bz2_file = bz2.BZ2File('file.bz2')
# bz2_file.read()

# gzip
import gzip
gzip_file = gzip.GzipFile('file.gz')
# gzip_file.read()

# lzma
import lzma
lzma_file = lzma.LZMAFile('file.xz')
# lzma_file.read()

# zlib
import zlib
zlib_file = zlib.decompress(open('file.z', 'rb').read())
# zlib_file

# tar
import tarfile
tar_file = tarfile.open('file.tar')
# tar_file.extractall()

# zip
import zipfile
zip_file = zipfile.ZipFile('file.zip')
# zip_file.extractall()

# rar
import rarfile
rar_file = rarfile.RarFile('file.rar')
# rar_file.extractall()

# 7z
import py
