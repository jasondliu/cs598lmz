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

# iso
import iso9660
iso9660.ISO9660(filename)

# dmg
import dmgfile
dmgfile.DmgFile(filename)

# mbr
import mbrfile
mbrfile.MbrFile(filename)

# ext
import extfile
extfile.ExtFile(filename)

# fat
import fatfile
fatfile.FatFile(filename)


