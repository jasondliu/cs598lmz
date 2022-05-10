import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import zlib
zlib.decompress(zlib.compress(b'Hello World'))

import lzma
lzma.decompress(lzma.compress(b'Hello World'))

import gzip
gzip.decompress(gzip.compress(b'Hello World'))

import zipfile
zf = zipfile.ZipFile('test.zip', 'w')
zf.write('test.py')
zf.close()

zf = zipfile.ZipFile('test.zip', 'r')
zf.extractall()
zf.close()

import tarfile
tf = tarfile.TarFile('test.tar', 'w')
tf.add('test.py')
tf.close()

tf = tarfile.TarFile('test.tar', 'r')
tf.extractall()
tf.close()

tf = tarfile.TarFile('test.tar.gz', 'w:gz')
tf.add
