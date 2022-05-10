import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

import cPickle
pickle.loads(pickle.dumps(dict(name='Bob', age=20, score=88)))

import marshal
marshal.dumps(dict(name='Bob', age=20, score=88))

import json
json.dumps(dict(name='Bob', age=20, score=88))
json.loads(json.dumps(dict(name='Bob', age=20, score=88)))

import struct
struct.pack('>I', 10240099)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
sha1.hexdig
