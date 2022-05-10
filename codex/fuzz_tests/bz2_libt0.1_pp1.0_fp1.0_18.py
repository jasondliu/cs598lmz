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

# iso
import pycdlib
pycdlib.PyCdlib()
pycdlib.PyCdlib.open(filename)

# dmg
import dmgbuild
dmgbuild.DMGMaker(filename)

# img
import img2py
img2py.img2py(filename)

# msi
import msilib
msilib.OpenDatabase(filename)

# cab
import cabextract
cabextract.cabextract(filename)

# deb
import debian.debfile
debian.debfile.DebFile(filename)
