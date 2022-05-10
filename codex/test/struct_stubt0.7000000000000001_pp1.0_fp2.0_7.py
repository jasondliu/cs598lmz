from _struct import Struct
s = Struct.__new__(Struct)
s.init(b'<h')
print(s.pack(1))
print(s.pack(2))
print(s.pack(3))
