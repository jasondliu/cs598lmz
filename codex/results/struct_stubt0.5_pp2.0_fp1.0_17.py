from _struct import Struct
s = Struct.__new__(Struct)
print(s)
print(s.size)
print(s.format)
print(s.unpack)
print(s.pack)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)
print(s.__class__)

print("\n\n")

class Struct(Struct):
    def __init__(self, format, *args):
        self.format = format
        self.size = struct.calcsize(format)
    def pack(self, *args):
        return struct.pack(self.format, *args)
    def unpack(self, *args):
        return struct.unpack(self.format, *args)

s = Struct("<hhl", 1, 2, 3)
print(s)
print(s.size)
print(s.format)
print(s.unpack)
print(s.pack)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)
print(s.__class
