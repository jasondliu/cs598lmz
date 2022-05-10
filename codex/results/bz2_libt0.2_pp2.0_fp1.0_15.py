import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import gzip
gzip.decompress(gzip.compress(b'hello world'))

import zipfile
zf = zipfile.ZipFile('test.zip', 'w')
zf.write('test.txt')
zf.close()

zf = zipfile.ZipFile('test.zip', 'r')
zf.read('test.txt')
zf.close()

import tarfile
tf = tarfile.TarFile('test.tar', 'w')
tf.add('test.txt')
tf.close()

tf = tarfile.TarFile('test.tar', 'r')
tf.extract('test.txt')
tf.close()

tf = tarfile.TarFile('test.tar', 'r')
tf.
