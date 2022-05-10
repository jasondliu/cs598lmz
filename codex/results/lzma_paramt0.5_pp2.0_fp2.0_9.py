from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 2.5.3 计算md5摘要
from hashlib import md5
m = md5()
m.update(b'Hello, world')
m.digest()
m.hexdigest()

m2 = md5()
m2.update(b'Hello, ')
m2.update(b'world')
m2.digest()

# 2.5.4 计算SHA1 摘要
from hashlib import sha1
s = sha1()
s.update(b'Hello, world')
s.digest()
s.hexdigest()

# 2.5.5 使用 RSA 加密算法
from Crypto.PublicKey import RSA
key = RSA.generate(2048)
key.exportKey('PEM')

# 2.5.6 使用数字签名
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_
