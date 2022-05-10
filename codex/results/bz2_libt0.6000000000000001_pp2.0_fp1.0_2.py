import bz2
bz2.BZ2File("file.bz2")

# gzip
import gzip
gzip.open("file.gz")

# lzma
import lzma
lzma.open("file.xz")

# tar
import tarfile
tarfile.open("file.tar")

# zip
import zipfile
zipfile.ZipFile("file.zip")

# rar
import rarfile
rarfile.RarFile("file.rar")

# 7z
import py7zr
py7zr.SevenZipFile("file.7z")

# ar
import arfile
arfile.ArFile("file.a")

# cpio
import cpiofile
cpiofile.CpioFile("file.cpio")

# iso
import iso9660
iso9660.ISO9660("file.iso")

# lha
import lzham
lzham.LzhamFile("file.lzh")

# squashfs
import squashfs
squashfs.SquashfsFile("file.squashfs")
