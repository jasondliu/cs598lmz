from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)  # b'\x01\x00\x00\x00'
s.unpack(b'\x01\x00\x00\x00')  # (1,)

# 用户自定义类型
class Point(object):
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point(x=%d, y=%d)' % (self.x, self.y)

s = Struct('i', 'i')
s.size  # 8
s.pack(1, 2)  # b'\x01\x00\x00\x00\x02\x00\x00\x00'
