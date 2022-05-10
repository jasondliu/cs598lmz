import bz2
bz2.decompress(file.read())

#unzip
import gzip
gzip.decompress(file.read())

#unzip
import lzma
lzma.decompress(file.read())

#unzip
import zlib
zlib.decompress(file.read(), 15+32)

#unzip
import zipfile
zipfile.ZipFile(file).extractall()

#unzip
import tarfile
tarfile.open(file).extractall()

#unzip
import rarfile
rarfile.RarFile(file).extractall()

#unzip
import arfile
arfile.ArFile(file).extractall()

#unzip
import cabfile
cabfile.CabFile(file).extractall()

#unzip
import lhafile
lhafile.LhaFile(file).extractall()

#unzip
import zooarchive
zooarchive.ZooFile(file).extractall()

#unzip
import cpio
cpio.
