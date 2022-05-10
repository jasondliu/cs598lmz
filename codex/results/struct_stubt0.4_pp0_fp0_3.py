from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 我们可以用它来构造一个结构体类，并使用它来解析二进制数据
import struct

class StructField:
    '''
    定义结构体域
    '''
    def __init__(self, format, offset):
        '''
        初始化
        '''
        self.format = format
        self.offset = offset
    def __get__(self, instance, cls):
        '''
        返回结构体域的值
        '''
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else
