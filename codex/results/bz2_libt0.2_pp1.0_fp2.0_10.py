import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rb')

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

# cpio
import cpiofile
cpiofile.CpioFile(filename)

# iso
import iso9660
iso9660.ISO9660(filename)

# dmg
import dmgfile
dmgfile.DmgFile(filename)

# msi
import msi
msi.MSI(filename)

# nes
import nesfile
nesfile.NesFile(filename)

# snes
import
