from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)
print(s.pack(123))
print(s.pack(123).decode('latin1'))
print(s.unpack(s.pack(123)))
print(s.unpack_from(s.pack(123)))
print(s.pack_into(bytes(4), 0, 123))
print(s.unpack_from(bytes(4), 0))


from _struct import Struct
s = Struct('i')
print(s.size)
print(s.pack(123))
print(s.pack(123).decode('latin1'))
print(s.unpack(s.pack(123)))
print(s.unpack_from(s.pack(123)))
print(s.pack_into(bytes(4), 0, 123))
print(s.unpack_from(bytes(4), 0))


from _struct import Struct
s = Struct('i')
print(s.size)
print(s.pack(123))
