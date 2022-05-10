from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<2s2h')

print(s.pack(b'ab', 1, 2))
