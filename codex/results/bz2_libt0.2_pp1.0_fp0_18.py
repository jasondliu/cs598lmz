import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import gzip
gzip.decompress(gzip.compress(b'hello world'))

import zipfile
z = zipfile.ZipFile('test.zip', 'w')
z.write('test.txt')
z.close()

z = zipfile.ZipFile('test.zip')
z.read('test.txt')
z.close()

import tarfile
t = tarfile.TarFile('test.tar', 'w')
t.add('test.txt')
t.close()

t = tarfile.TarFile('test.tar')
t.extractall()
t.close()

import os
os.system('ls')

import subprocess
subprocess.run(['ls', '-l'])

import tempfile
