from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 或者
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x01')

# 如果你想使用一个预先创建好的实例去解压多个字节字符串，你可以使用一个简单的生成器函数
from functools import partial
record_struct = Struct('>iif')

def unpack_records(format, data):
    record_size = record_struct.size
    r = iter(partial(record_struct.unpack_from, data, offset)
            for offset in range(0, len(data), record_size))
    return r

# unpack_records() 函
