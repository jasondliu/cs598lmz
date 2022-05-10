from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.decompress(bz2_data)

# base64

import base64
base64.b64encode(b'binary\x00string')

base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')

base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')

base64.urlsafe_b64decode('abcd--__')

# struct

import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

s = struct.Struct('>I')
s.pack(10240099)

s.unpack(b'\xf0\xf0\xf0\xf0')
