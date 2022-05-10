from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>3s3sHH'
s.size = s.calcsize(s.format)
print(s.size)

print(s.pack('abc', 'abc', 'abc', 1, 2))
print(s.unpack(_))
print(s.unpack_from(b'abcabcabc\0\0'))

import struct
print(struct.pack('>4sl', b'foo', 0xdeadbeef))
print(struct.unpack('>4sl', _))

# struct.pack_into()：将一个字节串封装到一个现有的字节串中，并返回修改后的长度
import binascii
buffer = bytearray(b'\0' * 16)
print(buffer)
struct.pack_into('>2sh', buffer, 0, 1, 2)
print(buffer)
print(binascii.hexlify(buffer
