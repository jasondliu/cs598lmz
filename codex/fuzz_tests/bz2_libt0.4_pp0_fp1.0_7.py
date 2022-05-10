import bz2
bz2.BZ2File('data/sherlock.txt.bz2').read()

import lzma
lzma.LZMAFile('data/sherlock.txt.xz').read()

import gzip
gzip.GzipFile('data/sherlock.txt.gz').read()

import zlib
zlib.decompress(open('data/sherlock.txt.z', 'rb').read())

import zipfile
zipfile.ZipFile('data/sherlock.txt.zip').read('sherlock.txt')

import tarfile
tarfile.open('data/sherlock.txt.tar').extractall()

import rarfile
rarfile.RarFile('data/sherlock.txt.rar').read('sherlock.txt')

import bz2
bz2.BZ2File('data/sherlock.txt.bz2').read()

import lzma
lzma.LZMAFile('data/sherlock.txt.xz').read()

import gzip
