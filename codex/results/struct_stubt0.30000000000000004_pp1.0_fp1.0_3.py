from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 使用struct模块来解析二进制数据
import struct
with open('myfile.zip', 'rb') as f:
    data = f.read()
start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)
    start += extra_size + comp_size

# 使用struct模块来打包数据
import struct
with open('myfile.zip', 'rb') as f:
    data =
