from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
print(s.size)

# 创建一个结构体实例
import binascii
packed_data = binascii.unhexlify('0100000061620000cdcc2c40')
print(s.unpack(packed_data))

# 将结构体打包为二进制数据
print(s.pack(b'\x01\x02', b'\x03\x04', 0x1234, 0x5678))

# 使用类方法
import struct
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size
