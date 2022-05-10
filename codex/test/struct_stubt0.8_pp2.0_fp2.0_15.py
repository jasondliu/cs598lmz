from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">I")

print(s.size)
print(s.pack(666))
