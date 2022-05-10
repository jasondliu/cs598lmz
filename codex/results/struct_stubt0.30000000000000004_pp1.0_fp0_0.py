from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 使用类的继承来实现结构体
class Struct(object):
    def __init__(self, format):
        self.format = format
    def __len__(self):
        return struct.calcsize(self.format)
    def pack(self, *args):
        return struct.pack(self.format, *args)
    def unpack(self, data):
        return struct.unpack(self.format, data)

# 使用类的继承来实现结构体
class Struct(object):
    def __init__(self, format):
        self.format = format
    def __len__(self):
        return struct.calcsize(self.format)
    def pack(self, *args):
        return struct.pack(self.format, *args)
    def unpack(self, data):
        return struct.un
