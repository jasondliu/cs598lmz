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
py7zlib.Archive7z(open(filename, 'rb'))

# cab
import pymspack
pymspack.mspack.Cabinet(filename)

# ar
import arfile
arfile.Archive(filename)

# iso
import pycdlib
pycdlib.PyCdlib()
pycdlib.PyCdlib().open(filename)

# dmg
import dmgbuild
dmgbuild.DMGMaster(filename)

# nsis
import pyinstaller.archive.nsis
pyinstaller.archive.nsis.NsisArchive(filename)

#
