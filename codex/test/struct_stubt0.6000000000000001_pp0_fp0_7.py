from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i",None,2)

with open("test.bin", "rb") as f:
    data = f.read()

r = s.unpack(data)
print(r)
