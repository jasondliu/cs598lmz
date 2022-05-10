from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.pack(1)

# 可以用_struct模块创建自定义类
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 50, 91.1)
print(s)

# _struct模块可以用来处理任意大小的二进制数据
# 把二进制数据打包成类似C语言的结构体
import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())
header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header))
del header
del img
