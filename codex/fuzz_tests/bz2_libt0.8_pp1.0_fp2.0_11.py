import bz2
bz2.BZ2File('data/enwik9', 'r')

import gzip
gzip.open('data/enwik9', 'r')

import lzma
lzma.LZMAFile('data/enwik9', 'r')

import zlib
zlib.decompressobj(wbits=32+15).decompress(line)

import tarfile
tar = tarfile.open('data/enwik9', 'r:gz')
members = tar.getmembers()
tar.extractall()
tar.extractall(path='/tmp/dir')
tar.extract('COPYING', '/tmp/dir')
tar.extract('README', '/tmp/dir', members=[members[2]])
for tarinfo in tar:
    print(tarinfo.name, tarinfo.size)

import zipfile
with zipfile.ZipFile('data/enwik9') as zf:
    with zf.open("README") as f:
        f.read()
    zf.extract('README', '/tmp/dir
