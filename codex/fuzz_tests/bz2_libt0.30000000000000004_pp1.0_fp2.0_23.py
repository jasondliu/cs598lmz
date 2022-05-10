import bz2
bz2.decompress(bz2.compress(b'hello world!'))

import gzip
gzip.compress(b'hello world!')

import zlib
zlib.compress(b'hello world!')

import hashlib
hashlib.md5(b'hello world!').hexdigest()

import hmac
hmac.new(b'key', b'hello world!', hashlib.sha1).hexdigest()

import base64
base64.b64encode(b'hello world!')

import struct
struct.pack('>I', 10240099)

import json
json.dumps([1, 'simple', 'list'])

import pickle
pickle.dumps([1, 'simple', 'list'])

import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:9000')
s.add(1, 2)

import urllib.request
response = urllib.request.urlopen('https://www.python.org')
html = response.read()

