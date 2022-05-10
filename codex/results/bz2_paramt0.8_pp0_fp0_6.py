from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s2)

#测试base64
def safe_base64_decode(s):
    if len(s) % 4 == 0:
        s = s + b'=='
    elif len(s) % 4 == 2:
        s = s + b'='
    return base64.b64decode(s)

#测试struct
import struct
struct.pack('>I', 10240099) #'>IH' 0x91234567
struct.unpack('>I', b'\x00\x9E\x01\x00')

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
struct.unpack('<ccIIIIII
