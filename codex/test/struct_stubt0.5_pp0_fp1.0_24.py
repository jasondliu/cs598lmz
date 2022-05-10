from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<10s"
s.size = s.format.size
print(s.size)

# 这样做的目的是为了给Struct定义一个类方法，可以通过类调用
def unpack(self, data):
    return self.format.unpack(data)

Struct.unpack = unpack
print(s.unpack(b'abcdefghij'))
