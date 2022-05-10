import lzma
lzma.LZMAFile(fileobj=open('test.xz', 'rb'))

import bz2
bz2.BZ2File(fileobj=open('test.bz2', 'rb'))

import gzip
gzip.GzipFile(fileobj=open('test.gz', 'rb'))

import zipfile
zf = zipfile.ZipFile(fileobj=open('test.zip', 'rb'))

import tarfile
tarfile.open(fileobj=open('test.tar', 'rb'))

#
# Test that we can write to a file opened with a different mode.
#

import io

f = io.open('test.txt', 'r')
f.write('test')

f = io.open('test.txt', 'w')
f.write('test')

f = io.open('test.txt', 'a')
f.write('test')

f = io.open('test.txt', 'r+')
f.write('test')

f = io.open('test.txt
