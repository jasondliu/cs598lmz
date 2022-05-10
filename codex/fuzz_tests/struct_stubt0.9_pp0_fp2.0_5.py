from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>300x')
b = b'abcdefg'
s.pack_into(b, 3, 123)
print(b)
print(s.unpack_from(b, 3))
