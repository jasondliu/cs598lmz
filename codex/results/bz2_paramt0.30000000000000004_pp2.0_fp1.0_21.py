from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(file_name, 'rb').read())

# gzip
import gzip
gzip.open(file_name, 'rb').read()

# lzma
import lzma
lzma.open(file_name, 'rb').read()

# tar
import tarfile
tarfile.open(file_name).extractall()

# zip
import zipfile
zipfile.ZipFile(file_name).extractall()

# tar.gz
import tarfile
import gzip
tarfile.open(gzip.open(file_name, 'rb')).extractall()

# tar.bz2
import tarfile
import bz2
tarfile.open(bz2.open(file_name, 'rb')).extractall()

# tar.xz
import tarfile
import lzma
tarfile.open(lzma.open(file_name, 'rb')).extractall()

# zip
import zipfile
zipfile.ZipFile(file_name).extractall()

#
