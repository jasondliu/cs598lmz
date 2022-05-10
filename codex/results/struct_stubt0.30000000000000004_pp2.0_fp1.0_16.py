from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# _struct.Struct.pack(format, v1, v2, ...)
# 根据给定的格式将数据打包成字符串
# _struct.Struct.unpack(format, buffer)
# 根据给定的格式将字符串解包成数据
# _struct.Struct.iter_unpack(format, buffer)
# 根据给定的格式将字符串解包成数据，返回一个迭代器

import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data
