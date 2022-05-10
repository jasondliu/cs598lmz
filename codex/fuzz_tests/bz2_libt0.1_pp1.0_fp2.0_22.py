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

# cpio
import cpiofile
cpiofile.Archive(filename)

# rpm
import rpm
rpm.open(filename)

# deb
import debfile
debfile.DebFile(filename)

# pax
import paxfile
paxfile.Archive(filename)

# iso9660
import iso9660
iso9660.Iso9660(filename)

# squashfs
import squashfs
squashfs.SquashFs(filename)


