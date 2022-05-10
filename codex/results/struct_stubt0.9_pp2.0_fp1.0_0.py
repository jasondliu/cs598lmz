from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<b>"
print(s.format)
print(Struct("<b"))

class MyStruct(Struct):
    def __new__(self):
        return Struct("<b")
print(MyStruct())

class IntByte(int):
    def __index__(self):
        return self
print(Byte("".encode("ascii"), 1))
