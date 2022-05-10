import bz2
bz2.decompress(bz2.compress(b"Hello World"))

#pickle
import pickle
pickle.dumps({"name": "Bob", "age": 20})
pickle.loads(b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x04\x00\x00\x00nameq\x02X\x03\x00\x00\x00Bobq\x03u.')

#json
import json
json.dumps({"name": "Bob", "age": 20})
json.loads('{"name": "Bob", "age": 20}')

#base64
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

#hmac
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key,
