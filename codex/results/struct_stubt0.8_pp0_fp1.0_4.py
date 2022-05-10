from _struct import Struct
s = Struct.__new__(Struct)
print(type(s))

# The next example illustrates this somewhat confusing behavior:


class MyStruct(Struct):
    _fields = [('x', 'i'), ('y', 'i')]

MyStruct._pack_ = Struct('ii').pack
MyStruct._unpack_ = Struct('ii').unpack

data = [1,2,3,4]
print(MyStruct._pack_(*data))
print(MyStruct._unpack_(b'\x01\x00\x00\x00\x04\x00\x00\x00'))
