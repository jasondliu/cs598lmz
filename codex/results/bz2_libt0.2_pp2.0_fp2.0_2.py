import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.TarFile(filename)

# rar
import rarfile
rarfile.RarFile(filename)

# 7z
import py7zlib
py7zlib.Archive7z(filename)

# cab
import cabextract
cabextract.Archive(filename)

# ar
import arfile
arfile.Archive(filename)

# rpm
import rpm
rpm.TransactionSet()

# deb
import dpkg
dpkg.DebFile(filename)

# cpio
import cpio
cpio.Archive(filename)

# iso
import pycdlib
pycdlib.PyCdlib()

# dmg
import dmgbuild
dmgbuild.DMG(filename)

# nsis
import
