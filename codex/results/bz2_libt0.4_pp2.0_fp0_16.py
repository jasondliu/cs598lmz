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

# 7z
import py7zlib
py7zlib.Archive7z(filename)

# rar
import rarfile
rarfile.RarFile(filename)

# ar
import arfile
arfile.ArFile(filename)

# cab
import cabfile
cabfile.CabFile(filename)

# lha
import lhafile
lhafile.LhaFile(filename)

# rpm
import rpmfile
rpmfile.RpmFile(filename)

# deb
import debfile
debfile.DebFile(filename)

# iso
import isofile
isofile.IsoFile(filename)

# nes
import nesfile
nesfile.NesFile(filename
