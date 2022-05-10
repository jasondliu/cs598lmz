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

# ar
import arfile
arfile.Archive(filename)

# cab
import cabfile
cabfile.Archive(filename)

# cpio
import cpiofile
cpiofile.Archive(filename)

# iso
import isofile
isofile.Archive(filename)

# lha
import lhafile
lhafile.Archive(filename)

# rpm
import rpmfile
rpmfile.Archive(filename)

# squashfs
import squashfile
squashfile.Archive(filename)

