from _struct import Struct
s = Struct.__new__(Struct)
print(s)

args = 'hhl' # 2 byte short, 2 byte short, 4 byte long
s.__init__(args)
print(s.size)
