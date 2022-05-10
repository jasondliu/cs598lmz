from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

# unpack
print(s.unpack(data))
# (1, b'ab', 2.7000000)

# unpack_from
print(s.unpack_from(data, 4))
# (1, b'ab', 2.7000000)
