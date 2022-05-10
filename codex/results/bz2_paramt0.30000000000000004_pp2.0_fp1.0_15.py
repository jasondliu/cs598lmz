from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

import struct
struct.pack('>I', 10240099)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

import hashlib
md5 = hashlib.md5()
md5.update(b'how to use md5 in python hashlib?')
md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update(b'how to use sha1 in ')
sha1.update(b'python hashlib?')
sha1.hexdigest()

db = {}

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8
