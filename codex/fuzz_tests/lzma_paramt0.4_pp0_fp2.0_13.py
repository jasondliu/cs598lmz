from lzma import LZMADecompressor
LZMADecompressor().decompress(open(file_name, 'rb').read())

# gzip
import gzip
gzip.open(file_name, 'rb').read()

# bz2
import bz2
bz2.BZ2File(file_name).read()

# zip
import zipfile
zipfile.ZipFile(file_name).read(zipfile.ZipFile(file_name).namelist()[0])

# tar
import tarfile
tarfile.open(file_name).extractall(path='./')

# rar
import rarfile
rarfile.RarFile(file_name).read(rarfile.RarFile(file_name).namelist()[0])

# 7z
import py7zlib
archive = py7zlib.Archive7z(open(file_name, 'rb'))
for name in archive.getnames():
    print(name)
    info = archive.getmember(name)
    print(info.read())

# cab
import cabfile
cabfile.CabFile
