from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes)

# xz
from lzma import open as lzopen
with lzopen('file.xz') as xz_file:
    data = xz_file.read()

# bz2
import bz2
with bz2.open('file.bz2', 'rt') as bz2_file:
    data = bz2_file.read()

# gzip
import gzip
with gzip.open('file.gz', 'rt') as gzip_file:
    data = gzip_file.read()

# tar
import tarfile
with tarfile.open('file.tar', 'r') as tar:
    for item in tar:
        print(item.name)
        print(item.size)

# zip
import zipfile
with zipfile.ZipFile('file.zip', 'r') as zip:
    print(zip.namelist())
    for info in zip.infolist():
        print(info.filename)
        print(info.file_size)
        print(info.
