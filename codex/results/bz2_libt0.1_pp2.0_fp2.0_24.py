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

# cab
import pymspack
pymspack.Cabinet(filename)

# ar
import arfile
arfile.Archive(filename)

# iso
import pycdlib
pycdlib.PyCdlib()
pycdlib.PyCdlib().open(filename)

# dmg
import dmgbuild
dmgbuild.DMG(filename)

# msi
import msi
msi.MSI(filename)

# swf
import swf
swf.SWF(filename)

# elf
import elftools
