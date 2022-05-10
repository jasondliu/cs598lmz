from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bb')
print(s.size)
print(s.pack(1, 2))
print(s.unpack(s.pack(1, 2)))
print(s.unpack_from(s.pack(1, 2)))

s = Struct.__new__(Struct)
s.__init__('bb', True)
print(s.size)
print(s.pack(1, 2))
print(s.unpack(s.pack(1, 2)))
print(s.unpack_from(s.pack(1, 2)))

s = Struct.__new__(Struct)
s.__init__('bb', False)
print(s.size)
print(s.pack(1, 2))
print(s.unpack(s.pack(1, 2)))
print(s.unpack_from(s.pack(1, 2)))

try:
  s = Struct.__new__(Struct)
  s.__init__('bb', 'a')
except TypeError:
  print('TypeError')
