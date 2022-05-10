from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x01\x01\x80\x02\xc0')

import bz2
bz2.decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x01\x01\x80\x02\xc0')


import lzma
lzma.decompress(b'X\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x0b\x05\x00\x00\x00')

# TAR
import tarfile
with tarfile.open('README.tar.gz') as t:
    t.extractall()

import tarfile
t = tarfile.open('README.tar.gz')
t.getnames()
t.extractall()
t.close()


import tarfile
t = tarfile.open('README.tar
