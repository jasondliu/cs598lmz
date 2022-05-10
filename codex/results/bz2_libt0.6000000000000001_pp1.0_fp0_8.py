import bz2
bz2.BZ2File(filename)

import gzip
gzip.GzipFile(filename)

import lzma
lzma.LZMAFile(filename)

import zipfile
zipfile.ZipFile(filename)
# create zip
import zipfile
with zipfile.ZipFile('file.zip','w') as myzip:
    myzip.write('file.txt')

# extract zip
import zipfile
with zipfile.ZipFile('file.zip','r') as myzip:
    myzip.extractall()

# extract zip
import zipfile
with zipfile.ZipFile('file.zip','r') as myzip:
    myzip.extract('file.txt')
    
# reading zip
import zipfile
with zipfile.ZipFile('file.zip','r') as myzip:
    myzip.open('file.txt')
 
# create tar
import tarfile
with tarfile.open('file.tar','w') as mytar:
    mytar.add('file.txt')

# extract tar
import tarfile
with
