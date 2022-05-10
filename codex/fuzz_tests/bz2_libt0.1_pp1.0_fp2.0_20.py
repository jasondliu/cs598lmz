import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

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

# ar
import arfile
arfile.Archive(filename)

# cab
import cabfile
cabfile.CabFile(filename)

# cpio
import cpiofile
cpiofile.CpioFile(filename)

# rpm
import rpmfile
rpmfile.RpmFile(filename)

# squashfs
import squashfs
squashfs.SquashFs(filename)

# swf
import swf
swf.SwfFile(filename)

# wim
import w
