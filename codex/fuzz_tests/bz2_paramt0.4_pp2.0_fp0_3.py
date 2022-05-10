from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

data = open('file.bz2', 'rb').read()
data[:4]

import bz2
bz2.decompress(data)

data = open('file.gz', 'rb').read()
data[:4]

from gzip import GzipFile
GzipFile(fileobj=StringIO(data)).read()

import gzip
gzip.decompress(data)

data = open('file.zip', 'rb').read()
data[:4]

from zipfile import ZipFile
ZipFile(StringIO(data)).read('file.txt')

import zipfile
zipfile.ZipFile(StringIO(data)).read('file.txt')

import tarfile
tar = tarfile.open('file.tar.gz', 'r:gz')
tar.extractall()
tar.close()

import zipfile
zip = zipfile.ZipFile('file.zip', 'r')
zip.extractall()
zip.close()

import bz2
bz2.BZ
