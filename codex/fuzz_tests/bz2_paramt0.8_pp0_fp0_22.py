from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_compressed_data)

# Base 64
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

# URL safe
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64decode('abcd--__')

# SHA1 for secure hashing
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))

