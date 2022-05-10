from _struct import Struct
s = Struct.__new__(Struct)
s.size = 8

print(s.size)
s.format = 'd'

double_struct = Struct('d')

double_struct.pack(1.23)

print(double_struct.pack(1.23))

double_struct.unpack(_)

double_struct.unpack(_)

print(double_struct.unpack(_))
