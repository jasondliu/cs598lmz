from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
print(s.size)

t = Struct.__new__(Struct)
print(t.size)

t.__init__('I 2s f')
print(t.size)

s = Struct('I 2s f')
s.size

s = Struct('I 2s f')
s.pack(1234, b'ab', 2.7)

s = Struct('I 2s f')
s.pack_into(bytes(12), 0, 1234, b'ab', 2.7)

s = Struct('I 2s f')
buffer = bytes(12)
s.pack_into(buffer, 0, 1234, b'ab', 2.7)
s.pack_into(buffer, 6, 4321, b'cd', 3.14)
print(buffer)

s = Struct('I 2s f')
buffer = bytearray(12)
s.pack_into(buffer, 0, 1234, b'ab', 2.7)
