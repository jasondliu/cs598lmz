from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xf6\x2c')

import lzma
lzma.open('/tmp/foo.xz')

# tarfile
import tarfile
tar = tarfile.open('example.tar')
tar.getmember('README.txt')
tar.extractall()
tar.close()

import tarfile
with tarfile.open('example.tar') as t:
    for member_info in t.getmembers():
        print(member_info.name)

import tarfile
with tarfile.open('example.tar') as t:
    for member_info in t.getmembers():
        t.extract(member_info)

import tarfile
with tarfile.open('example.tar') as t:
    for member_info in t.getmembers():
        t.extract(member_info, path='/tmp/example')

import tarfile
with tarfile.open('example.tar') as t
