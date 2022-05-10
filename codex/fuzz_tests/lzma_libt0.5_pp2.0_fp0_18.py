import lzma
lzma.decompress(lzma.compress(b'hello world'))

# base64
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

# struct
import struct
struct.pack('>I', 10240099)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# hashlib
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.hexdigest()

# hmac
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
h.hexdigest()

# itertools
import itertools
natuals = itertools.count(1)
for n in natual
