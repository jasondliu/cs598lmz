from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# _struct.Struct.pack(format, v1, v2, ...)
# _struct.Struct.unpack(format, buffer)
# _struct.Struct.iter_unpack(format, buffer)

import binascii

s = Struct('I 2s f')
packed_data = s.pack(1, b'ab', 2.7)
print(packed_data)
print(binascii.hexlify(packed_data))

data = s.unpack(packed_data)
print(data)

for p in s.iter_unpack(b'\x00\x00\x00\x01ab\x00\x00\x00\x00\x00\x00(B'):
    print(p)

# 大端法和小端法
# 大端法：高位字节排放在内存的低地
