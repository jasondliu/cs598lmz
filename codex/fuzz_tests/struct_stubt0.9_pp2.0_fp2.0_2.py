from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">L"
d = s.unpack(x)[0]
print date.fromtimestamp(d).__str__()

s = Struct(">L")
d = s.unpack(x)[0]
print date.fromtimestamp(d).__str__()
