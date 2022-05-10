from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

data = s.pack(1,False,3.1415926)
s.unpack(data)

#制作自己的格式化类

import sys

class StructField:
    '''
    定义结构域的一些基本属性，一个结构化域对象可以追踪类型码，和其他格式信息
    '''
    def __init__(self, fmt, offset):
        self.fmt = fmt
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.fmt,instance._buffer,self.offset)
