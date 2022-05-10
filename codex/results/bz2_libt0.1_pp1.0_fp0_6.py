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
cabfile.Archive(filename)

# cpio
import cpiofile
cpiofile.Archive(filename)

# iso
import iso9660
iso9660.ISO9660(filename)

# lha
import lzhamodule
lzhamodule.LZHAFile(filename)

# rpm
import rpm
rpm.addMacro('_binary_payload', 'w
