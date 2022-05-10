from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

print(s.size)
print(s.pack(1, b'ab', 2.7))
