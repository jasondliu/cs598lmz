from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = calcsize(s.format)
s.pack_into(buf, 0, 1, 2, 3)
print(buf)
print(s.unpack_from(buf, 0))

# 构建一个结构体类
from _struct import Struct

class StructField:
    '''
    descr: 字段描述符
    offset: 字段偏移量
    format: 字段格式
    '''
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            r = instance._buffer[self.offset:self.offset + calcsize(self.format)]
            return unpack(self.format, r)[0]
    def __set__(self, instance
