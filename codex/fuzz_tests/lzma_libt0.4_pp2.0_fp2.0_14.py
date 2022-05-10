import lzma
lzma.open('./data/lzma/lzma.txt.lzma')

# gzip
import gzip
gzip.open('./data/gzip/gzip.txt.gz')

# bz2
import bz2
bz2.open('./data/bz2/bz2.txt.bz2')

# tar
import tarfile
tar = tarfile.open('./data/tar/tar.tar')
tar.extractall()
tar.close()

# zip
import zipfile
zip = zipfile.ZipFile('./data/zip/zip.zip')
zip.extractall()
zip.close()

# rar
import rarfile
rar = rarfile.RarFile('./data/rar/rar.rar')
rar.extractall()
rar.close()

# 7z
import py7zlib
archive = py7zlib.Archive7z(open('./data/7z/7z.7z', 'rb'))
for name in archive
