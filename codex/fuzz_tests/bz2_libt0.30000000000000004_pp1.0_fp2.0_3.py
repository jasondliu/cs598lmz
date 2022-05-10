import bz2
bz2.BZ2File(path)

# gzip
import gzip
gzip.open(path)

# lzma
import lzma
lzma.open(path)

# zip
import zipfile
zipfile.ZipFile(path)

# tar
import tarfile
tarfile.open(path)

# rar
import rarfile
rarfile.RarFile(path)

# 7z
import py7zlib
py7zlib.Archive7z(open(path, 'rb'))

# xz
import lzma
lzma.open(path)

# ar
import arfile
arfile.Archive(path)

# cab
import cabfile
cabfile.CabFile(path)

# cpio
import cpiofile
cpiofile.CpioFile(path)

# iso
import iso9660
iso9660.ISO9660(path)

# lzh
import lzhlib
lzhlib.LzhFile(path)

# rpm
import rpm
rpm
