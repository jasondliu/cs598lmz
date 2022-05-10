from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2s2s'
s.size = s.calcsize(s.format)
print(s.size)
print(s.pack('ab', b'\x00', b'\x01'))

# 创建一个类，它的实例将被用作上面的Struct对象
class Struct(Struct):
    def __init__(self, format, *args):
        self.format = format
        self.size = self.calcsize(format)
        self.unpack(args)
    def unpack(self, *args):
        self.data = self.pack(*args)
    def pack(self, *args):
        return Struct.pack(self.format, *args)
    def __iter__(self):
        return iter(Struct.unpack(self.format, self.data))

# 使用自定义的Struct类
s = Struct('<2s2s', b
