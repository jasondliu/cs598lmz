from lzma import LZMADecompressor
LZMADecompressor().decompress(base64.b64decode(s))

# eval
eval(base64.b64decode(s))

# 反序列化
# pickle
import pickle
pickle.loads(base64.b64decode(s))

# json
import json
json.loads(base64.b64decode(s))

# 加密
# base64
import base64
base64.b64encode(s)

# md5
import hashlib
hashlib.md5(s).hexdigest()

# sha1
import hashlib
hashlib.sha1(s).hexdigest()

# 二进制转换
# hex
hex(int(s, 16))

# bin
bin(int(s, 2))

# chr
chr(int(s, 16))

# str
str(int(s, 8))

# int
int(s, 16)

# 判断类型
