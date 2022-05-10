from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bbbb')
print(s.size)
print(s.unpack_from(b'abcd',0))

v = b'abcd'
print(len(v))
print(''.join(map(chr, v)))
print()

v = b'abcd'
print(len(v))
print([ord(c) for c in v])
print()

v = b'abcd'
for i in v:
    print(i)

v = b'abcd'
for i in v:
    print(i, chr(i))
print()

v = b'abcd'
fmt = '4si4s4si'
s = Struct(fmt)
print(s.size)
ret = s.pack(*(v, 1, v, 2))
print(ret)
print(s.unpack(ret))
