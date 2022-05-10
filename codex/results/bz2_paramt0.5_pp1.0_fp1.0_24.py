from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc4\x8d\x06\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# 7.2.2 字节到大整数的打包与解包
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
len(data)

int.from_bytes(data, 'little')
int.from_bytes(data, 'big')

x = 94522842520747284487117727783387188
x.to_bytes(16, 'big')
x.to_bytes(16, 'little')

import struct
hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo


