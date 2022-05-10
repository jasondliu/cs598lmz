from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 下面是一个使用字节流来解析网络协议的例子
from collections import namedtuple
import struct

# 定义一个结构体
# 其中包含一个32位的整数和一个浮点数
_P = namedtuple('Point', ['x', 'y'])

class Point(_P):
    __slots__ = ()
    def __str__(self):
        return 'Point({}, {})'.format(self.x, self.y)

def get_struct(byteorder='>'):
    return struct.Struct(byteorder + '2d')

def unpack(data):
    return Point(*get_struct().unpack(data))

#
