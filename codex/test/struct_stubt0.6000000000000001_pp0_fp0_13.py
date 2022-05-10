from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

with open('in.bin', 'rb') as f:
    f.seek(0x20)
    print(s.unpack(f.read(s.size)))
