import bz2
bz2.decompress(bz2.compress(b'hello world'))

import gzip
gzip.compress(b'hello world')

import zlib
zlib.compress(b'hello world')

import hashlib
hashlib.md5(b'hello world').hexdigest()

import hmac
hmac.new(b'123', b'hello world', 'md5').hexdigest()

import random
random.random()

import struct
struct.pack('>I', 10240099)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

import json
json.dumps([1, 'simple', 'list'])
json.loads('{"a": 1, "b": 2, "c": 3}')

import pickle
d = dict
