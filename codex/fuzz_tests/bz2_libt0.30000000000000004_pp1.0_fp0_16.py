import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

import zlib
zlib.decompress(zlib.compress(b'Hello World!'))

import hashlib
hashlib.md5(b'Hello World!').hexdigest()

import hmac
hmac.new(b'Hello World!', digestmod='MD5').hexdigest()

import base64
base64.b64encode(b'Hello World!')

import json
json.dumps([1, 2, 3, {'4': 5, '6': 7}])

import pickle
pickle.dumps([1, 2, 3, {'4': 5, '6': 7}])

import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:9000')
s.pow(2, 3)
s.add(2, 3)
s.div(5, 2)

import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y
