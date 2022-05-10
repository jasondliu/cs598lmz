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

# cab
import cabfile
cabfile.CabFile(filename)

# ar
import arfile
arfile.ArFile(filename)

# iso
import pycdlib
pycdlib.PyCdlib()
pycdlib.PyCdlib.open(filename)

# dmg
import dmgbuild
dmgbuild.DMG(filename)

# nsis
import pyinstaller
pyinstaller.archive.NSISArchive(filename)

# elf
import elftools
elftools.elf.elffile.ELFF
