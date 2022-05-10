import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rb')

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
pymspack.CabFile(filename)

# ar
import arfile
arfile.ArFile(filename)

# iso
import pycdlib
pycdlib.PyCdlib()
iso.open_file(filename)

# dmg
import dmgbuild
dmgbuild.DMG(filename)

# rpm
import rpm
rpm.TransactionSet()
ts.open_rpm_file(filename)

# cpio
import cpiofile
cpiofile.C
