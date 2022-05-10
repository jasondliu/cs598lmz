import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# Encode/Decode Base64
import base64
base64.b64encode(b'Hello World!')
base64.b64decode(b'SGVsbG8gV29ybGQh')

# URLSafe Base64
base64.urlsafe_b64encode(b'Hello World!')
base64.urlsafe_b64decode(b'SGVsbG8gV29ybGQh')

# Hash MD5
import hashlib
md5 = hashlib.md5()
md5.update(b'Hello')
md5.update(b'World')
md5.digest()

# Hash SHA1
import hashlib
sha1 = hashlib.sha1()
sha1.update(b'Hello')
sha1.update(b'World')
sha1.digest()

# HMAC
import hmac
h = hmac.new(b'123456', digestmod='md5')
h.update(b'
