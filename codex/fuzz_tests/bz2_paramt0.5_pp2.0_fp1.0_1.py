from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# Use the zlib module to compress data.
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# Use base64 encoding and decoding.
import base64
s = b'hello'
a = base64.b64encode(s)
a
base64.b64decode(a)

# Use struct to pack data into bytes.
import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# Use hashlib to calculate message digest.
import hashlib
md5 = hashlib.md5()
md5.update(b'how to use md5 in python hashlib?')
md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update
