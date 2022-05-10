import lzma
lzma.decompress(lzma.compress(b'Hello World'))

import zipfile
zf = zipfile.ZipFile('archive.zip', 'w')
zf.write('README.txt')
zf.write('hello.py')
zf.close()
zf = zipfile.ZipFile('archive.zip', 'r')
zf.namelist()
zf.read('README.txt')
zf.close()

import tarfile
tf = tarfile.TarFile('archive.tar', 'w')
tf.add('README.txt')
tf.add('hello.py')
tf.close()
tf = tarfile.TarFile('archive.tar', 'r')
tf.getnames()
tf.extractall()
tf.close()

import gzip
gzip.compress(b'Hello World')

import bz2
bz2.compress(b'Hello World')

import zlib
zlib.compress(b'Hello World')

import sys
sys.stdout.write('Hello World
