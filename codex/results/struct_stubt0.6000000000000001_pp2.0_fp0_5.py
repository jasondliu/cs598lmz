from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = Struct.calcsize(s.format)
print(s.size)
print(s.format)

class Struct(Struct):
    def __init__(self, format, *args):
        self.format = format
        self.size = Struct.calcsize(format)
        self.unpack(args)
    def pack(self, *args):
        return Struct.pack(self.format, *args)
    def unpack(self, *args):
        return Struct.unpack(self.format, *args)
    def __len__(self):
        return self.size

print(Struct('I').size)
