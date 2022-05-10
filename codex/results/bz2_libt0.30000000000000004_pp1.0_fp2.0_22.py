import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import zlib
zlib.decompress(zlib.compress(b'Hello World'))

import json
json.dumps([1, 'simple', 'list'])

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

import pickle
pickle.dumps([1, 2, 3])

pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03e.')

import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how
