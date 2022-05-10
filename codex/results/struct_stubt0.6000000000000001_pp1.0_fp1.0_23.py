from _struct import Struct
s = Struct.__new__(Struct)

s.__init__('123456789')

print(s.size)
print(s.format)
print(s.unpack('abcdefghi'))
print(s.pack('abcdefghi'))

print('test2')

s = Struct('123456789')

print(s.size)
print(s.format)
print(s.unpack('abcdefghi'))
print(s.pack('abcdefghi'))

print('test3')

s = Struct('123456789')

print(s.size)
print(s.format)
print(s.unpack('abcdefghi'))
print(s.pack('abcdefghi'))

print('test4')

s = Struct('123456789')

print(s.size)
print(s.format)
print(s.unpack('abcdefghi'))
print(s.pack('abcdefghi'))

print('test5')

s = Struct('123456789')


