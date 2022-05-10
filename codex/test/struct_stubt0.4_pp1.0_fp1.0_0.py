from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = s.calcsize(s.format)
print(s.size)

# 使用一个类来记录文件中的格式信息
import struct

class StructField:
    '''
    定义一个类来描述结构体中的字段
    '''
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

