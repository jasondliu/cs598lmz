from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

import bz2
bz2.decompress(data)

# tar
# tarfile

import tarfile
tf = tarfile.open('output/xxx.tar.gz')

# zip
# zipfile

import zipfile
zf = zipfile.ZipFile('output/xxx.zip')

# stringio, bytesio

from io import StringIO
f = StringIO()
f.write('hello')
f.write('xxx')
f.getvalue()

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
f.getvalue()


# struct
import struct
struct.pack('>I', 10240099)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# hashlib

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
