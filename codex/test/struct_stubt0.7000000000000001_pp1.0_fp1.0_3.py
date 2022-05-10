from _struct import Struct
s = Struct.__new__(Struct)
s.format = "H"
s.size = calcsize(s.format)

f = open("subject.dat", "rb")
f.seek(0x0)
f.seek(0x16)

a = f.read(1)
b = f.read(1)

f.close()

print(unpack(s.format, bytes(b) + bytes(a)))
# (1,)
