import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename).read()

# lzma
import lzma
lzma.open(filename).read()

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

# iso9660
import pycdlib
pycdlib.PyCdlib().open(filename).read()

# dmg
import dmgbuild
dmgbuild.read(filename)

# cpio
import cpio
cpio.CpioFile(filename).read()

# squashfs
import pytsk3
pytsk3.Img_Info(filename).read()

# cramfs
import pytsk3
pytsk3.Img_Info(filename).read()
