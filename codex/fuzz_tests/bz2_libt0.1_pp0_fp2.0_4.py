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
iso9660.Iso9660(filename)

# dmg
import dmgfile
dmgfile.DmgFile(filename)

# msi
import msi
msi.MSI(filename)

# cab
import cabfile
cabfile.CabFile(filename)

# swf
import swf
swf.SWF(filename)

